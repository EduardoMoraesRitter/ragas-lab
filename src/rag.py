"""Dois RAGs de brinquedo sobre o mesmo corpus.

- "bom":  busca por embedding (gemini-embedding-001), top-3 trechos.
- "ruim": busca por contagem de palavras em comum, sem tirar stopwords, top-2.
          Erra de propósito: palavras como "a", "de", "da" dominam a nota.

Saída: data/respostas-<modo>.json com pergunta, contextos usados e resposta.
Uso: python src/rag.py bom | ruim | ambos
"""
from __future__ import annotations

import json
import math
import re
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

RAIZ = Path(__file__).resolve().parent.parent
load_dotenv(RAIZ / ".env")

import os  # noqa: E402

LLM_MODEL = os.environ["LLM_MODEL"]
EMBED_MODEL = os.environ["EMBED_MODEL"]
cliente = OpenAI(max_retries=8)  # usa OPENAI_API_KEY e OPENAI_BASE_URL do .env; 8 tentativas com espera para 429

SYSTEM = (
    "Você é o assistente de suporte da Caffeo Brasil. Responda em português, em até 3 frases, "
    "usando SOMENTE os trechos fornecidos. Se os trechos não trouxerem a informação, "
    "responda exatamente: 'Não encontrei essa informação nas fontes disponíveis.'"
)


def carregar_corpus() -> list[dict]:
    trechos = []
    for arq in sorted((RAIZ / "corpus").glob("*.md")):
        fonte = arq.stem
        texto = arq.read_text(encoding="utf-8")
        partes = re.split(r"^## ", texto, flags=re.M)[1:]
        for i, parte in enumerate(partes):
            titulo, _, corpo = parte.partition("\n")
            trechos.append({
                "id": f"{fonte}-{i+1:02d}",
                "fonte": fonte,
                "titulo": titulo.strip(),
                "texto": f"{titulo.strip()}. {corpo.strip()}",
            })
    return trechos


def tokens(s: str) -> list[str]:
    return re.findall(r"\w+", s.lower())


# ---------- busca ruim: palavras em comum, com stopwords ----------
def buscar_ruim(pergunta: str, trechos: list[dict], k: int = 2) -> list[dict]:
    q = tokens(pergunta)
    def nota(t):
        tt = tokens(t["texto"])
        return sum(tt.count(w) for w in q)
    return sorted(trechos, key=nota, reverse=True)[:k]


# ---------- busca boa: embeddings ----------
def embed(textos: list[str]) -> list[list[float]]:
    r = cliente.embeddings.create(model=EMBED_MODEL, input=textos)
    return [d.embedding for d in r.data]


def cos(a, b):
    return sum(x*y for x, y in zip(a, b)) / (math.sqrt(sum(x*x for x in a)) * math.sqrt(sum(y*y for y in b)))


def embeddings_corpus(trechos: list[dict]) -> dict[str, list[float]]:
    cache = RAIZ / "data" / "embeddings.json"
    if cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))
    vecs = embed([t["texto"] for t in trechos])
    mapa = {t["id"]: v for t, v in zip(trechos, vecs)}
    cache.write_text(json.dumps(mapa), encoding="utf-8")
    return mapa


def buscar_bom(pergunta: str, trechos: list[dict], mapa, k: int = 3) -> list[dict]:
    qv = embed([pergunta])[0]
    return sorted(trechos, key=lambda t: cos(qv, mapa[t["id"]]), reverse=True)[:k]


# ---------- geração ----------
def responder(pergunta: str, contextos: list[dict]) -> str:
    bloco = "\n\n".join(f"[{c['id']}] {c['texto']}" for c in contextos)
    r = cliente.chat.completions.create(
        model=LLM_MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": f"Trechos:\n{bloco}\n\nPergunta: {pergunta}"},
        ],
    )
    return r.choices[0].message.content.strip()


def rodar(modo: str):
    trechos = carregar_corpus()
    perguntas = json.loads((RAIZ / "data" / "perguntas.json").read_text(encoding="utf-8"))
    mapa = embeddings_corpus(trechos) if modo == "bom" else None
    saida = []
    for p in perguntas:
        ctx = buscar_bom(p["pergunta"], trechos, mapa) if modo == "bom" else buscar_ruim(p["pergunta"], trechos)
        resp = responder(p["pergunta"], ctx); time.sleep(float(os.environ.get("PAUSA_S", "2")))
        saida.append({
            **p,
            "modo": modo,
            "contextos_ids": [c["id"] for c in ctx],
            "contextos": [c["texto"] for c in ctx],
            "resposta": resp,
        })
        print(f"[{modo}] {p['id']} ctx={[c['id'] for c in ctx]}\n   -> {resp[:120]}")
    (RAIZ / "data" / f"respostas-{modo}.json").write_text(
        json.dumps(saida, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "ambos"
    for m in (["bom", "ruim"] if modo == "ambos" else [modo]):
        rodar(m)
