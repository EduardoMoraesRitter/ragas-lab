"""Junta results/{ragas,deepeval,promptfoo}.json e gera as tabelas de docs/tabelas.md.

O texto de análise fica em docs/RELATORIO.md, escrito à mão. Aqui só números.
"""
from __future__ import annotations

import json
from statistics import mean

from comum import RAIZ

FERRAMENTAS = ["ragas", "deepeval", "promptfoo"]
ORDEM_TECNICAS = ["ruim", "bom", "bm25", "arvore", "agentico", "grafo"]
NOME_TECNICA = {"ruim": "palavras (ruim)", "bom": "vetor (bom)", "bm25": "BM25", "arvore": "árvore", "agentico": "agêntico", "grafo": "grafo"}
METRICAS = ["faithfulness", "answer_relevancy", "context_precision", "context_recall"]
ROTULO = {
    "faithfulness": "Fidelidade",
    "answer_relevancy": "Relevância da resposta",
    "context_precision": "Precisão do contexto",
    "context_recall": "Cobertura do contexto",
}


def fmt(v):
    return "–" if v is None else f"{v:.2f}"


def main():
    dados = {}
    for f in FERRAMENTAS:
        for arq in sorted((RAIZ / "results").glob(f"{f}*.json")):
            conteudo = json.loads(arq.read_text(encoding="utf-8"))
            if not isinstance(conteudo, list):  # promptfoo-raw*.json é o bruto do Promptfoo
                continue
            for linha in conteudo:
                dados[(f, linha["modo"], linha["id"])] = linha
    modos = sorted({m for (_, m, _) in dados}, key=lambda m: (ORDEM_TECNICAS.index(m) if m in ORDEM_TECNICAS else 99, m))
    respostas = {}
    for modo in modos:
        for r in json.loads((RAIZ / "data" / f"respostas-{modo}.json").read_text(encoding="utf-8")):
            respostas[(modo, r["id"])] = r

    out = ["# Tabelas geradas (src/relatorio.py)\n"]

    # 1. Média por ferramenta x modo x métrica
    out.append("## 1. Média por ferramenta e por técnica de busca\n")
    out.append("| Ferramenta | Técnica | " + " | ".join(ROTULO[m] for m in METRICAS) + " |")
    out.append("|---|---|" + "---|" * len(METRICAS))
    for f in FERRAMENTAS:
        for modo in modos:
            medias = []
            for m in METRICAS:
                vals = [dados[(f, modo, q)]["scores"].get(m) for q in [f"q{i}" for i in range(1, 9)] if (f, modo, q) in dados]
                vals = [v for v in vals if v is not None]
                medias.append(mean(vals) if vals else None)
            if all(v is None for v in medias):
                continue
            out.append(f"| {f} | {NOME_TECNICA.get(modo, modo)} | " + " | ".join(fmt(v) for v in medias) + " |")
    out.append("")

    # 2. Por pergunta: as 3 ferramentas lado a lado, uma tabela por métrica
    for m in METRICAS:
        out.append(f"## 2. {ROTULO[m]} por pergunta (" + " / ".join(NOME_TECNICA.get(x, x) for x in modos) + ")\n")
        out.append("| Pergunta | " + " | ".join(FERRAMENTAS) + " |")
        out.append("|---|" + "---|" * len(FERRAMENTAS))
        for i in range(1, 9):
            q = f"q{i}"
            celulas = []
            for f in FERRAMENTAS:
                celulas.append(" / ".join(fmt(dados.get((f, modo, q), {}).get("scores", {}).get(m)) for modo in modos))
            out.append(f"| {q} | " + " | ".join(celulas) + " |")
        out.append("")

    # 3. Respostas e contextos, para leitura humana
    out.append("## 3. O que cada RAG respondeu\n")
    for i in range(1, 9):
        q = f"q{i}"
        p = respostas[(modos[0], q)]
        out.append(f"### {q}. {p['pergunta']}\n")
        out.append(f"Gabarito: {p['referencia']}\n")
        for modo in modos:
            r = respostas[(modo, q)]
            out.append(f"- **{NOME_TECNICA.get(modo, modo)}** (trechos {', '.join(r['contextos_ids'])}): {r['resposta']}")
        out.append("")

    # 4. Motivos dados pelos juízes (quando a ferramenta devolve)
    out.append("## 4. Motivos dados pelo juiz (DeepEval e Promptfoo devolvem; Ragas não)\n")
    for f in ("deepeval", "promptfoo"):
        for modo in modos:
            for i in range(1, 9):
                q = f"q{i}"
                d = dados.get((f, modo, q))
                if not d:
                    continue
                for m in METRICAS:
                    motivo = (d.get("detalhes") or {}).get(m)
                    if motivo:
                        out.append(f"- {f} / {modo} / {q} / {ROTULO[m]} = {fmt(d['scores'].get(m))}: {str(motivo).strip()[:400]}")
    out.append("")

    destino = RAIZ / "docs" / "tabelas.md"
    destino.write_text("\n".join(out), encoding="utf-8")
    print("gerado", destino)


if __name__ == "__main__":
    main()
