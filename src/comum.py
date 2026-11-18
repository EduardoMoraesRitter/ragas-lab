"""Carrega .env e as respostas dos dois RAGs. Usado pelos três avaliadores."""
from __future__ import annotations

import json
import os
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent.parent
load_dotenv(RAIZ / ".env")

API_KEY = os.environ["OPENAI_API_KEY"]
BASE_URL = os.environ["OPENAI_BASE_URL"]
LLM_MODEL = os.environ["LLM_MODEL"]
EMBED_MODEL = os.environ["EMBED_MODEL"]
PAUSA_S = float(os.environ.get("PAUSA_S", "2"))


TECNICAS = os.environ.get("TECNICAS", "bom,ruim").split(",")
SUFIXO = "" if os.environ.get("TECNICAS") is None else "-" + "-".join(TECNICAS)


def carregar_respostas() -> list[dict]:
    """Respostas das técnicas em TECNICAS (env; padrão bom,ruim), concatenadas."""
    linhas = []
    for modo in TECNICAS:
        arq = RAIZ / "data" / f"respostas-{modo}.json"
        linhas += json.loads(arq.read_text(encoding="utf-8"))
    return linhas


def salvar_resultado(nome: str, linhas: list[dict]) -> Path:
    """results/<ferramenta><sufixo>.json; sufixo = técnicas avaliadas (vazio no padrão bom,ruim)."""
    destino = RAIZ / "results" / f"{nome}{SUFIXO}.json"
    destino.write_text(json.dumps(linhas, ensure_ascii=False, indent=2), encoding="utf-8")
    return destino
