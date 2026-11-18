"""Gera promptfooconfig.yaml a partir das respostas prontas e converte o
results/promptfoo-raw.json do Promptfoo para o mesmo formato dos outros.

Uso:
  python src/promptfoo_config.py gerar      -> promptfooconfig.yaml
  npx promptfoo eval -c promptfooconfig.yaml --env-file .env --output results/promptfoo-raw.json --no-cache
  python src/promptfoo_config.py converter  -> results/promptfoo.json
"""
from __future__ import annotations

import json
import sys

from comum import BASE_URL, EMBED_MODEL, LLM_MODEL, RAIZ, SUFIXO, carregar_respostas, salvar_resultado

SEP = "\n\n---\n\n"  # separador entre trechos recuperados

MAPA = {
    "context-faithfulness": "faithfulness",
    "answer-relevance": "answer_relevancy",
    "context-relevance": "context_precision",  # equivalente mais próximo: contexto é relevante à pergunta?
    "context-recall": "context_recall",
}


def gerar():
    import yaml  # type: ignore

    testes = []
    for r in carregar_respostas():
        testes.append({
            "description": f"{r['modo']}-{r['id']}",
            "vars": {
                "modo": r["modo"],
                "id": r["id"],
                "query": r["pergunta"],
                "response": r["resposta"],
                # uma string só: lista em var vira N casos de teste no Promptfoo (expansão cartesiana)
                "context": SEP.join(r["contextos"]),
            },
            "assert": [
                {"type": "context-faithfulness", "threshold": 0.5},
                {"type": "answer-relevance", "threshold": 0.5},
                {"type": "context-relevance", "threshold": 0.5},
                {"type": "context-recall", "value": r["referencia"], "threshold": 0.5},
            ],
        })
    cfg = {
        "description": "ragas-lab: avaliar respostas RAG já geradas (bom x ruim)",
        "prompts": ["{{response}}"],
        "providers": ["echo"],
        "defaultTest": {
            "options": {
                "provider": {
                    "text": {"id": f"openai:chat:{LLM_MODEL}",
                             "config": {"apiBaseUrl": BASE_URL.rstrip("/"), "apiKey": "{{env.OPENAI_API_KEY}}", "temperature": 0}},
                    "embedding": {"id": f"openai:embedding:{EMBED_MODEL}",
                                  "config": {"apiBaseUrl": BASE_URL.rstrip("/"), "apiKey": "{{env.OPENAI_API_KEY}}"}},
                }
            }
        },
        "tests": testes,
    }
    destino = RAIZ / f"promptfooconfig{SUFIXO}.yaml"
    destino.write_text(yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print("gerado", destino, f"({len(testes)} testes)")


def converter():
    bruto = json.loads((RAIZ / "results" / f"promptfoo-raw{SUFIXO}.json").read_text(encoding="utf-8"))
    resultados = bruto["results"]["results"] if isinstance(bruto["results"], dict) else bruto["results"]
    saida = []
    for res in resultados:
        v = res.get("vars") or res.get("testCase", {}).get("vars", {})
        linha = {"modo": v["modo"], "id": v["id"], "ferramenta": "promptfoo", "scores": {}, "detalhes": {}}
        comps = (res.get("gradingResult") or {}).get("componentResults") or []
        for c in comps:
            tipo = (c.get("assertion") or {}).get("type")
            nome = MAPA.get(tipo, tipo)
            motivo = c.get("reason") or ""
            # juiz não devolveu o formato que o Promptfoo espera: fica sem nota, como nos outros dois
            falhou = c.get("score") is None or "Grader returned no" in motivo or "invalid" in motivo.lower()
            linha["scores"][nome] = None if falhou else round(float(c["score"]), 3)
            linha["detalhes"][nome] = ("ERRO do juiz: " + motivo) if falhou else motivo
        saida.append(linha)
    saida.sort(key=lambda x: (x["modo"], x["id"]))
    print("salvo em", salvar_resultado("promptfoo", saida), f"({len(saida)} linhas)")


if __name__ == "__main__":
    {"gerar": gerar, "converter": converter}[sys.argv[1]]()
