"""RAGs de brinquedo sobre o mesmo corpus: só a BUSCA muda, o gerador é o mesmo.

Técnicas (data/respostas-<tecnica>.json):
- ruim:     palavras em comum, com stopwords, top-2. Erra de propósito (piso).
- bom:      embedding (gemini-embedding-001), top-3. Era o "RAG bom".
- bm25:     BM25 Okapi sobre palavras sem stopwords, top-3. Sem LLM na busca.
- arvore:   estilo PageIndex, sem vetor: índice com título e resumo por seção;
            o LLM lê o sumário e escolhe até 3 seções. 1 chamada por pergunta.
- agentico: o LLM tem ferramentas (listar, grep, ler) e busca em até 6 passos.

Uso: python src/rag.py bom | ruim | bm25 | arvore | agentico | todas
"""
from __future__ import annotations

import json
import math
import re
import sys
import time
from collections import Counter
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

RAIZ = Path(__file__).resolve().parent.parent
load_dotenv(RAIZ / ".env")

import os  # noqa: E402

LLM_MODEL = os.environ["LLM_MODEL"]
EMBED_MODEL = os.environ["EMBED_MODEL"]
PAUSA_S = float(os.environ.get("PAUSA_S", "2"))
cliente = OpenAI(max_retries=8)  # usa OPENAI_API_KEY e OPENAI_BASE_URL do .env; 8 tentativas com espera para 429

SYSTEM = (
    "Você é o assistente de suporte da Caffeo Brasil. Responda em português, em até 3 frases, "
    "usando SOMENTE os trechos fornecidos. Se os trechos não trouxerem a informação, "
    "responda exatamente: 'Não encontrei essa informação nas fontes disponíveis.'"
)

STOPWORDS = set("""a o as os um uma uns umas de da do das dos em na no nas nos por para com sem sobre
e ou mas que se é ser foi são ao à às aos como qual quais quanto quanta quantos quantas quando onde
eu tu ele ela nós vós eles elas me te lhe meu minha seu sua sua teu tua este esta esse essa isso isto
aquele aquela aquilo há tem ter tenho tinha pode posso devo deve já não sim mais menos muito pouco
também até entre antes depois hoje ainda só cada qualquer todo toda todos todas""".split())


def chamar_llm(mensagens: list[dict], temperature: float = 0) -> str:
    r = cliente.chat.completions.create(model=LLM_MODEL, temperature=temperature, messages=mensagens)
    return (r.choices[0].message.content or "").strip()


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


def tokens_limpos(s: str) -> list[str]:
    return [w for w in tokens(s) if w not in STOPWORDS and len(w) > 1]


# ---------- ruim: palavras em comum, com stopwords ----------
def buscar_ruim(pergunta: str, trechos: list[dict], k: int = 2) -> list[dict]:
    q = tokens(pergunta)
    def nota(t):
        tt = tokens(t["texto"])
        return sum(tt.count(w) for w in q)
    return sorted(trechos, key=nota, reverse=True)[:k]


# ---------- bom: embeddings ----------
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


def buscar_bom(pergunta: str, trechos: list[dict], k: int = 3) -> list[dict]:
    mapa = embeddings_corpus(trechos)
    qv = embed([pergunta])[0]
    return sorted(trechos, key=lambda t: cos(qv, mapa[t["id"]]), reverse=True)[:k]


# ---------- bm25: palavra exata, sem stopwords (BM25 Okapi, k1=1.5, b=0.75) ----------
def buscar_bm25(pergunta: str, trechos: list[dict], k: int = 3) -> list[dict]:
    docs = [tokens_limpos(t["texto"]) for t in trechos]
    n = len(docs)
    avg = sum(len(d) for d in docs) / n
    df = Counter(w for d in docs for w in set(d))
    q = tokens_limpos(pergunta)
    def nota(i):
        tf = Counter(docs[i]); dl = len(docs[i]); s = 0.0
        for w in q:
            if w not in tf:
                continue
            idf = math.log(1 + (n - df[w] + 0.5) / (df[w] + 0.5))
            s += idf * tf[w] * 2.5 / (tf[w] + 1.5 * (1 - 0.75 + 0.75 * dl / avg))
        return s
    ordem = sorted(range(n), key=nota, reverse=True)
    return [trechos[i] for i in ordem[:k] if nota(i) > 0] or [trechos[i] for i in ordem[:k]]


# ---------- arvore: sumário com resumos, o LLM escolhe as seções (estilo PageIndex) ----------
def indice_arvore(trechos: list[dict]) -> dict:
    """Uma vez: resumo de 1 frase por seção, gerado pelo LLM, guardado em data/arvore.json."""
    cache = RAIZ / "data" / "arvore.json"
    if cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))
    arvore = {}
    for fonte in sorted({t["fonte"] for t in trechos}):
        secoes = [t for t in trechos if t["fonte"] == fonte]
        bloco = "\n\n".join(f"[{t['id']}] {t['texto']}" for t in secoes)
        txt = chamar_llm([
            {"role": "system", "content": "Você monta o índice de um documento. Para cada seção, escreva um resumo de UMA frase, "
                                          "em português, dizendo que informações ela contém (números, nomes, regras). "
                                          "Responda só com JSON: {\"<id>\": \"<resumo>\", ...}."},
            {"role": "user", "content": bloco},
        ])
        m = re.search(r"\{.*\}", txt, flags=re.S)
        resumos = json.loads(m.group(0)) if m else {}
        arvore[fonte] = [{"id": t["id"], "titulo": t["titulo"], "resumo": resumos.get(t["id"], t["titulo"])} for t in secoes]
        time.sleep(PAUSA_S)
    cache.write_text(json.dumps(arvore, ensure_ascii=False, indent=2), encoding="utf-8")
    return arvore


def buscar_arvore(pergunta: str, trechos: list[dict], k: int = 3) -> list[dict]:
    arvore = indice_arvore(trechos)
    sumario = "\n".join(
        f"# {fonte}\n" + "\n".join(f"  [{s['id']}] {s['titulo']}: {s['resumo']}" for s in secoes)
        for fonte, secoes in arvore.items())
    txt = chamar_llm([
        {"role": "system", "content": "Você recebe o sumário de 3 documentos (só títulos e resumos, não o texto) e uma pergunta. "
                                      f"Raciocine em qual seção a resposta deve estar e devolva os ids de até {k} seções, "
                                      "da mais provável para a menos. Responda só com JSON: {\"ids\": [\"...\"]}."},
        {"role": "user", "content": f"Sumário:\n{sumario}\n\nPergunta: {pergunta}"},
    ])
    m = re.search(r"\{.*\}", txt, flags=re.S)
    ids = json.loads(m.group(0)).get("ids", []) if m else []
    por_id = {t["id"]: t for t in trechos}
    return [por_id[i] for i in ids if i in por_id][:k]


# ---------- agentico: o LLM busca com ferramentas, em vários passos ----------
def buscar_agentico(pergunta: str, trechos: list[dict], k: int = 3, max_passos: int = 6) -> list[dict]:
    por_id = {t["id"]: t for t in trechos}
    ferramentas = {
        "listar": lambda _arg: "\n".join(f"[{t['id']}] {t['titulo']}" for t in trechos),
        "grep": lambda arg: "\n".join(
            f"[{t['id']}] ...{m.group(0)}..." for t in trechos
            for m in [re.search(r".{0,60}" + re.escape(arg) + r".{0,60}", t["texto"], flags=re.I)] if m) or "(nada encontrado)",
        "ler": lambda arg: f"[{arg}] {por_id[arg]['texto']}" if arg in por_id else "(id inexistente)",
    }
    msgs = [
        {"role": "system", "content":
            "Você é um agente de busca. Seu objetivo é achar as seções de um corpus que respondem à pergunta. "
            "Ferramentas: listar (ids e títulos de todas as seções), grep <termo> (seções onde o termo aparece), "
            "ler <id> (texto completo da seção). Uma ação por vez. Responda SÓ com JSON: "
            "{\"acao\": \"listar\"} | {\"acao\": \"grep\", \"arg\": \"termo\"} | {\"acao\": \"ler\", \"arg\": \"id\"} | "
            f"{{\"acao\": \"pronto\", \"ids\": [até {k} ids, do melhor para o pior]}}. "
            f"Você tem no máximo {max_passos} ações antes de precisar responder pronto. "
            "Se nenhuma seção responder, devolva pronto com as seções mais próximas do assunto."},
        {"role": "user", "content": f"Pergunta: {pergunta}"},
    ]
    lidos: list[str] = []
    for passo in range(max_passos + 1):
        if passo == max_passos:
            msgs.append({"role": "user", "content": "Acabaram as ações. Responda pronto agora."})
        txt = chamar_llm(msgs)
        msgs.append({"role": "assistant", "content": txt})
        m = re.search(r"\{.*\}", txt, flags=re.S)
        try:
            acao = json.loads(m.group(0)) if m else {}
        except json.JSONDecodeError:
            acao = {}
        if acao.get("acao") == "pronto" or passo == max_passos:
            ids = [i for i in acao.get("ids", []) if i in por_id] or lidos[-k:]
            return [por_id[i] for i in ids][:k]
        nome = acao.get("acao"); arg = str(acao.get("arg", ""))
        if nome == "ler" and arg in por_id:
            lidos.append(arg)
        resultado = ferramentas[nome](arg) if nome in ferramentas else "(ação inválida; use listar, grep, ler ou pronto)"
        msgs.append({"role": "user", "content": f"Resultado de {nome} {arg}:\n{resultado[:3000]}"})
        time.sleep(PAUSA_S)
    return []


# ---------- grafo: GraphRAG em memória (networkx), sem Neo4j ----------
def indice_grafo(trechos: list[dict]):
    """Uma vez: o LLM extrai triplas (sujeito, relação, objeto) de cada seção, 1 chamada por documento.
    Guardado em data/grafo.json. Nó = entidade; aresta guarda a relação e o id da seção de onde veio."""
    import networkx as nx

    cache = RAIZ / "data" / "grafo.json"
    if cache.exists():
        triplas = json.loads(cache.read_text(encoding="utf-8"))
    else:
        triplas = []
        for fonte in sorted({t["fonte"] for t in trechos}):
            secoes = [t for t in trechos if t["fonte"] == fonte]
            bloco = "\n\n".join(f"[{t['id']}] {t['texto']}" for t in secoes)
            txt = chamar_llm([
                {"role": "system", "content":
                    "Você extrai um grafo de conhecimento. Para cada seção [id], liste triplas (sujeito, relação, objeto) "
                    "com entidades concretas: produto, modelo, pessoa, empresa, peça, código de erro, número, prazo, regra. "
                    "Nomes de entidade curtos e consistentes entre seções (ex.: 'Aurora K2', 'garantia', 'descalcificação', 'erro E2'). "
                    "Responda só com JSON: [{\"s\": \"...\", \"r\": \"...\", \"o\": \"...\", \"id\": \"<id da seção>\"}, ...]"},
                {"role": "user", "content": bloco},
            ])
            m = re.search(r"\[.*\]", txt, flags=re.S)
            triplas += json.loads(m.group(0)) if m else []
            time.sleep(PAUSA_S)
        cache.write_text(json.dumps(triplas, ensure_ascii=False, indent=1), encoding="utf-8")
    g = nx.Graph()
    for tr in triplas:
        s, o, sec = str(tr.get("s", "")).strip().lower(), str(tr.get("o", "")).strip().lower(), tr.get("id")
        if not s or not o or not sec:
            continue
        g.add_node(s); g.add_node(o)
        g.add_edge(s, o)
        g[s][o].setdefault("fatos", []).append((tr.get("r", ""), sec))
    return g


def buscar_grafo(pergunta: str, trechos: list[dict], k: int = 3) -> list[dict]:
    """Busca local estilo GraphRAG: acha os nós citados na pergunta, anda 1 salto, e devolve as seções
    de onde vieram as arestas tocadas (as mais tocadas primeiro)."""
    g = indice_grafo(trechos)
    q = {w[:5] for w in tokens_limpos(pergunta)}  # prefixo de 5 letras: "descalcificar" casa com "descalcificação"
    def casa(no):  # nó casa com a pergunta se alguma palavra forte do nó está na pergunta
        return any(w[:5] in q for w in tokens_limpos(no) if len(w) > 2)
    sementes = [n for n in g.nodes if casa(n)]
    pontos: Counter = Counter()
    for s in sementes:
        peso_s = 1 / g.degree(s)  # nó-hub ("aurora k2") aparece em tudo e vale pouco
        for viz in g.neighbors(s):
            peso = peso_s * (2 if viz in sementes else 1)
            for _, sec in g[s][viz]["fatos"]:
                pontos[sec] += peso
    por_id = {t["id"]: t for t in trechos}
    ids = [sec for sec, _ in pontos.most_common(k) if sec in por_id]
    return [por_id[i] for i in ids] or buscar_bm25(pergunta, trechos, k)


TECNICAS = {
    "ruim": buscar_ruim,
    "bom": buscar_bom,
    "bm25": buscar_bm25,
    "arvore": buscar_arvore,
    "agentico": buscar_agentico,
    "grafo": buscar_grafo,
}


# ---------- geração (igual para todas) ----------
def responder(pergunta: str, contextos: list[dict]) -> str:
    bloco = "\n\n".join(f"[{c['id']}] {c['texto']}" for c in contextos) or "(nenhum trecho)"
    return chamar_llm([
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": f"Trechos:\n{bloco}\n\nPergunta: {pergunta}"},
    ])


def rodar(tecnica: str):
    buscar = TECNICAS[tecnica]
    trechos = carregar_corpus()
    perguntas = json.loads((RAIZ / "data" / "perguntas.json").read_text(encoding="utf-8"))
    saida = []
    t0 = time.time()
    for p in perguntas:
        ctx = buscar(p["pergunta"], trechos)
        resp = responder(p["pergunta"], ctx); time.sleep(PAUSA_S)
        saida.append({
            **p,
            "modo": tecnica,
            "contextos_ids": [c["id"] for c in ctx],
            "contextos": [c["texto"] for c in ctx],
            "resposta": resp,
        })
        print(f"[{tecnica}] {p['id']} ctx={[c['id'] for c in ctx]}\n   -> {resp[:120]}", flush=True)
    (RAIZ / "data" / f"respostas-{tecnica}.json").write_text(
        json.dumps(saida, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[{tecnica}] {time.time()-t0:.0f}s", flush=True)


if __name__ == "__main__":
    alvo = sys.argv[1] if len(sys.argv) > 1 else "todas"
    for t in (list(TECNICAS) if alvo == "todas" else alvo.split(",")):
        rodar(t)
