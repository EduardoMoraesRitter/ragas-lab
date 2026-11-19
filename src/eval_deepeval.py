"""Avalia as respostas dos dois RAGs com DeepEval 4.x.

Métricas: FaithfulnessMetric, AnswerRelevancyMetric, ContextualPrecisionMetric,
ContextualRecallMetric. Saída: results/deepeval.json
"""
from __future__ import annotations

import os
import time

os.environ.setdefault("DEEPEVAL_TELEMETRY_OPT_OUT", "YES")

import json  # noqa: E402

from comum import API_KEY, BASE_URL, LLM_MODEL, PAUSA_S, RAIZ, SUFIXO, carregar_respostas, salvar_resultado  # noqa: E402

from deepeval.metrics import (  # noqa: E402
    AnswerRelevancyMetric,
    ContextualPrecisionMetric,
    ContextualRecallMetric,
    FaithfulnessMetric,
)
from deepeval.models import OpenAIModel  # noqa: E402
from deepeval.test_case import LLMTestCase  # noqa: E402


def main():
    juiz = OpenAIModel(
        model=LLM_MODEL,
        api_key=API_KEY,
        base_url=BASE_URL,
        temperature=0,
        cost_per_input_token=0.0,
        cost_per_output_token=0.0,
    )
    comuns = dict(model=juiz, threshold=0.5, include_reason=True, async_mode=False)
    fabricas = {
        "faithfulness": lambda: FaithfulnessMetric(**comuns),
        "answer_relevancy": lambda: AnswerRelevancyMetric(**comuns),
        "context_precision": lambda: ContextualPrecisionMetric(**comuns),
        "context_recall": lambda: ContextualRecallMetric(**comuns),
    }

    # Retomada: se o arquivo de saída já existe, reaproveita as notas válidas e só refaz as vazias (ex.: 429 de cota)
    anteriores = {}
    arq_saida = RAIZ / "results" / f"deepeval{SUFIXO}.json"
    if arq_saida.exists():
        anteriores = {(x["modo"], x["id"]): x for x in json.loads(arq_saida.read_text(encoding="utf-8"))}

    saida = []
    t0 = time.time()
    for r in carregar_respostas():
        caso = LLMTestCase(
            input=r["pergunta"],
            actual_output=r["resposta"],
            expected_output=r["referencia"],
            retrieval_context=r["contextos"],
        )
        linha = anteriores.get((r["modo"], r["id"])) or {"modo": r["modo"], "id": r["id"], "ferramenta": "deepeval", "scores": {}, "detalhes": {}}
        for nome, fabrica in fabricas.items():
            if linha["scores"].get(nome) is not None:
                continue
            # Limite por minuto do nível gratuito: no 429, espera e tenta de novo
            for tentativa in range(4):
                m = fabrica()
                try:
                    m.measure(caso)
                    linha["scores"][nome] = round(float(m.score), 3)
                    linha["detalhes"][nome] = m.reason
                    break
                except Exception as e:  # noqa: BLE001
                    linha["scores"][nome] = None
                    linha["detalhes"][nome] = f"ERRO: {type(e).__name__}: {str(e)[:200]}"
                    if "429" not in str(e) or tentativa == 3:
                        break
                    time.sleep(40)
            time.sleep(PAUSA_S)
        print(f"[deepeval] {r['modo']:4s} {r['id']} {linha['scores']}")
        saida.append(linha)
    print(f"tempo total: {time.time()-t0:.0f}s")
    print("salvo em", salvar_resultado("deepeval", saida))


if __name__ == "__main__":
    main()
