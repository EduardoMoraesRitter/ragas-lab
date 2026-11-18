"""Exporta os resultados para a página do portfólio (Astro).

Lê results/<ferramenta>*.json e data/respostas-<tecnica>.json e grava um JSON compacto,
pronto para o build do site, no caminho passado como argumento.

Uso: python src/exportar_site.py ../eduardomoraesritter.github.io/src/data/ragas-lab/resultados.json
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

from comum import RAIZ

FERRAMENTAS = ["ragas", "deepeval", "promptfoo"]
METRICAS = ["context_precision", "context_recall", "faithfulness", "answer_relevancy"]
TECNICAS = ["arvore", "agentico", "bom", "bm25", "grafo", "ruim"]
# chamadas de LLM na busca, por pergunta (o índice da árvore e do grafo é feito uma vez só)
CUSTO_BUSCA = {
    "ruim": {"llm": "0", "indice": "—"},
    "bom": {"llm": "0", "indice": "embedding de 30 trechos"},
    "bm25": {"llm": "0", "indice": "—"},
    "arvore": {"llm": "1", "indice": "3 chamadas (resumo por seção)"},
    "agentico": {"llm": "2 a 7", "indice": "—"},
    "grafo": {"llm": "0", "indice": "3 chamadas (triplas)"},
}


def carregar_resultados():
    dados = {}
    for f in FERRAMENTAS:
        for arq in sorted((RAIZ / "results").glob(f"{f}*.json")):
            conteudo = json.loads(arq.read_text(encoding="utf-8"))
            if isinstance(conteudo, list):
                for linha in conteudo:
                    dados[(f, linha["modo"], linha["id"])] = linha
    return dados


def media(vals):
    vals = [v for v in vals if v is not None]
    return round(sum(vals) / len(vals), 3) if vals else None


def corta(txt, n=420):
    if not txt:
        return None
    txt = " ".join(str(txt).split())
    return txt if len(txt) <= n else txt[: n - 1].rstrip() + "…"


def main(destino: Path):
    dados = carregar_resultados()
    perguntas = json.loads((RAIZ / "data" / "perguntas.json").read_text(encoding="utf-8"))
    respostas = {t: {r["id"]: r for r in json.loads((RAIZ / "data" / f"respostas-{t}.json").read_text(encoding="utf-8"))}
                 for t in TECNICAS}

    medias = {}  # medias[tecnica][ferramenta][metrica]
    for t in TECNICAS:
        medias[t] = {}
        for f in FERRAMENTAS:
            linha = {m: media([dados.get((f, t, p["id"]), {}).get("scores", {}).get(m) for p in perguntas]) for m in METRICAS}
            if any(v is not None for v in linha.values()):
                medias[t][f] = linha

    saida_perguntas = []
    for p in perguntas:
        item = {"id": p["id"], "pergunta": p["pergunta"], "referencia": p["referencia"], "fontes": p.get("fontes", []),
                "tipo": p.get("tipo", ""), "tecnicas": {}}
        for t in TECNICAS:
            r = respostas[t][p["id"]]
            notas = {}
            for f in FERRAMENTAS:
                d = dados.get((f, t, p["id"]))
                if d and any(v is not None for v in d["scores"].values()):  # linha só com erro (ex.: cota) fica de fora
                    notas[f] = {m: {"v": d["scores"].get(m), "motivo": corta((d.get("detalhes") or {}).get(m))} for m in METRICAS}
            item["tecnicas"][t] = {"trechos": r["contextos_ids"], "resposta": r["resposta"], "notas": notas}
        saida_perguntas.append(item)

    pacote = {
        "gerado": date.today().isoformat(),
        "repositorio": "https://github.com/EduardoMoraesRitter/ragas-lab",
        "ferramentas": FERRAMENTAS,
        "metricas": METRICAS,
        "tecnicas": TECNICAS,
        "custo_busca": CUSTO_BUSCA,
        "medias": medias,
        "perguntas": saida_perguntas,
        "corpus": {"fontes": 3, "trechos": 30, "perguntas": len(perguntas)},
    }
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(pacote, ensure_ascii=False, indent=1), encoding="utf-8")
    print("gerado", destino, f"({destino.stat().st_size // 1024} KB)")
    for t in TECNICAS:
        print(t, {f: medias[t][f] for f in medias[t]})


if __name__ == "__main__":
    main(Path(sys.argv[1]))
