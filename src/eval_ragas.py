"""Avalia as respostas dos dois RAGs com Ragas 0.4 (API collections, ascore).

Métricas: faithfulness, answer_relevancy, context_precision (com referência),
context_recall (com referência). Saída: results/ragas.json
"""
from __future__ import annotations

import asyncio
import time

from openai import AsyncOpenAI

from comum import API_KEY, BASE_URL, EMBED_MODEL, LLM_MODEL, PAUSA_S, carregar_respostas, salvar_resultado

from ragas.embeddings.base import embedding_factory
from ragas.llms import llm_factory
from ragas.metrics.collections import AnswerRelevancy, ContextPrecision, ContextRecall, Faithfulness


async def main():
    client = AsyncOpenAI(api_key=API_KEY, base_url=BASE_URL, max_retries=8)
    llm = llm_factory(LLM_MODEL, provider="openai", client=client)
    emb = embedding_factory("openai", model=EMBED_MODEL, client=client)

    metricas = {
        "faithfulness": Faithfulness(llm=llm),
        "answer_relevancy": AnswerRelevancy(llm=llm, embeddings=emb),
        "context_precision": ContextPrecision(llm=llm),
        "context_recall": ContextRecall(llm=llm),
    }

    saida = []
    t0 = time.time()
    for r in carregar_respostas():
        linha = {"modo": r["modo"], "id": r["id"], "ferramenta": "ragas", "scores": {}, "detalhes": {}}
        for nome, m in metricas.items():
            kwargs = dict(user_input=r["pergunta"], response=r["resposta"], retrieved_contexts=r["contextos"])
            if nome == "answer_relevancy":
                kwargs = dict(user_input=r["pergunta"], response=r["resposta"])
            if nome in ("context_precision", "context_recall"):
                kwargs["reference"] = r["referencia"]
            try:
                res = await m.ascore(**kwargs)
                linha["scores"][nome] = round(float(res.value), 3)
                linha["detalhes"][nome] = getattr(res, "reason", None)
            except Exception as e:  # noqa: BLE001
                linha["scores"][nome] = None
                linha["detalhes"][nome] = f"ERRO: {type(e).__name__}: {str(e)[:200]}"
            await asyncio.sleep(PAUSA_S)
        print(f"[ragas] {r['modo']:4s} {r['id']} {linha['scores']}")
        saida.append(linha)
    print(f"tempo total: {time.time()-t0:.0f}s")
    print("salvo em", salvar_resultado("ragas", saida))


if __name__ == "__main__":
    asyncio.run(main())
