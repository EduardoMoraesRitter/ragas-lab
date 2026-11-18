"""Gera docs/comparativo.html: gráficos de barras (4 métricas x 3 ferramentas x 2 RAGs)
e tabela por pergunta com os motivos do juiz. Página estática, sem dependência externa.

Uso: python src/pagina.py  -> docs/comparativo.html
"""
from __future__ import annotations

import json
from datetime import date

from comum import RAIZ

FERRAMENTAS = ["ragas", "deepeval", "promptfoo"]
METRICAS = ["faithfulness", "answer_relevancy", "context_precision", "context_recall"]
ROTULO = {
    "faithfulness": "Fidelidade",
    "answer_relevancy": "Relevância da resposta",
    "context_precision": "Precisão do contexto",
    "context_recall": "Cobertura do contexto",
}
EXPLICA = {
    "faithfulness": "A resposta só diz coisas que estão nos trechos recuperados?",
    "answer_relevancy": "A resposta fala do que foi perguntado?",
    "context_precision": "Os trechos recuperados são os certos para a pergunta?",
    "context_recall": "Os trechos recuperados cobrem o gabarito inteiro?",
}
JUIZ = {"ragas": "gemini-3.5-flash-lite", "deepeval": "gemini-3.5-flash-lite", "promptfoo": "gemini-3.1-flash-lite"}


def carregar():
    dados = {}
    for f in FERRAMENTAS:
        arq = RAIZ / "results" / f"{f}.json"
        if arq.exists():
            for linha in json.loads(arq.read_text(encoding="utf-8")):
                dados.setdefault(f, {})[(linha["modo"], linha["id"])] = linha
    respostas = {}
    for modo in ("bom", "ruim"):
        for r in json.loads((RAIZ / "data" / f"respostas-{modo}.json").read_text(encoding="utf-8")):
            respostas[(modo, r["id"])] = r
    return dados, respostas


def montar_dados(dados, respostas):
    """Estrutura compacta para o JS da página."""
    perguntas = []
    for i in range(1, 9):
        q = f"q{i}"
        p = respostas[("bom", q)]
        item = {"id": q, "pergunta": p["pergunta"], "referencia": p["referencia"], "tipo": p.get("tipo", ""), "modos": {}}
        for modo in ("bom", "ruim"):
            r = respostas[(modo, q)]
            m = {"resposta": r["resposta"], "contextos_ids": r["contextos_ids"], "contextos": r["contextos"], "scores": {}, "motivos": {}}
            for f in FERRAMENTAS:
                linha = dados.get(f, {}).get((modo, q))
                if not linha:
                    continue
                m["scores"][f] = linha["scores"]
                m["motivos"][f] = {k: (str(v) if v else None) for k, v in (linha.get("detalhes") or {}).items()}
            item["modos"][modo] = m
        perguntas.append(item)
    medias = {}
    for f in FERRAMENTAS:
        for modo in ("bom", "ruim"):
            for met in METRICAS:
                vals = [dados[f][(modo, f"q{i}")]["scores"].get(met) for i in range(1, 9) if f in dados and (modo, f"q{i}") in dados[f]]
                vals = [v for v in vals if v is not None]
                medias[f"{f}|{modo}|{met}"] = (sum(vals) / len(vals)) if vals else None
    return {"perguntas": perguntas, "medias": medias, "ferramentas": [f for f in FERRAMENTAS if f in dados],
            "metricas": METRICAS, "rotulo": ROTULO, "explica": EXPLICA, "juiz": JUIZ, "gerado": date.today().isoformat()}


HTML = r"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ragas x DeepEval x Promptfoo</title>
<style>
:root{
  color-scheme: light;
  --page:#f9f9f7; --surface:#fcfcfb; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --grid:#e1e0d9; --axis:#c3c2b7; --border:rgba(11,11,11,.10);
  --bom:#2a78d6; --ruim:#eb6834;
  --seq1:#cde2fb; --seq2:#9ec5f4; --seq3:#6da7ec; --seq4:#3987e5; --seq5:#256abf; --seq6:#184f95;
  --vazio:#f0efec;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    color-scheme: dark;
    --page:#0d0d0d; --surface:#1a1a19; --ink:#f0efec; --ink2:#c3c2b7; --muted:#898781;
    --grid:#2c2c2a; --axis:#383835; --border:rgba(255,255,255,.10);
    --bom:#3987e5; --ruim:#d95926;
    --seq1:#0d366b; --seq2:#104281; --seq3:#1c5cab; --seq4:#256abf; --seq5:#3987e5; --seq6:#6da7ec;
    --vazio:#383835;
  }
}
:root[data-theme="dark"]{
  color-scheme: dark;
  --page:#0d0d0d; --surface:#1a1a19; --ink:#f0efec; --ink2:#c3c2b7; --muted:#898781;
  --grid:#2c2c2a; --axis:#383835; --border:rgba(255,255,255,.10);
  --bom:#3987e5; --ruim:#d95926;
  --seq1:#0d366b; --seq2:#104281; --seq3:#1c5cab; --seq4:#256abf; --seq5:#3987e5; --seq6:#6da7ec;
  --vazio:#383835;
}
*{box-sizing:border-box}
body{margin:0;background:var(--page);color:var(--ink);font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:1100px;margin:0 auto;padding:32px 16px 64px}
h1{font-size:26px;margin:0 0 4px;font-weight:650}
h2{font-size:19px;margin:40px 0 8px;font-weight:650}
p{margin:6px 0;color:var(--ink2)}
.sub{color:var(--muted);font-size:13px}
.legenda{display:flex;gap:18px;align-items:center;margin:14px 0 6px;font-size:13px;color:var(--ink2)}
.sw{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:6px;vertical-align:-1px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.card{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:14px 14px 8px}
.card h3{margin:0 0 2px;font-size:14px;font-weight:650}
.card .exp{margin:0 0 8px;font-size:12px;color:var(--muted)}
svg text{font-family:inherit;fill:var(--ink2);font-size:11px}
svg .tick{fill:var(--muted);font-variant-numeric:tabular-nums}
svg .gl{stroke:var(--grid);stroke-width:1}
svg .ax{stroke:var(--axis);stroke-width:1}
svg .val{fill:var(--ink);font-size:11px;font-variant-numeric:tabular-nums}
.bar{cursor:pointer}
.bar:hover{filter:brightness(1.12)}
.tip{position:fixed;pointer-events:none;background:var(--surface);color:var(--ink);border:1px solid var(--border);
  border-radius:8px;padding:8px 10px;font-size:12px;max-width:380px;box-shadow:0 4px 18px rgba(0,0,0,.18);display:none;z-index:9;white-space:pre-wrap}
table{border-collapse:separate;border-spacing:0;width:100%;background:var(--surface);border:1px solid var(--border);border-radius:10px;overflow:hidden;font-size:13px}
th,td{padding:7px 8px;text-align:left;border-bottom:1px solid var(--grid);vertical-align:top}
th{font-weight:600;color:var(--ink2);background:var(--surface);position:sticky;top:0}
th.g{text-align:center;border-left:1px solid var(--grid)}
td.c{text-align:center;font-variant-numeric:tabular-nums;width:46px;cursor:pointer}
td.c.first{border-left:1px solid var(--grid)}
td.c span{display:inline-block;min-width:38px;padding:2px 4px;border-radius:5px;color:#fff}
td.c span.escuro{color:#0b0b0b}
tr:last-child td{border-bottom:none}
.tabs{display:flex;gap:6px;margin:10px 0}
.tabs button{background:var(--surface);color:var(--ink);border:1px solid var(--border);border-radius:999px;padding:5px 14px;cursor:pointer;font:inherit;font-size:13px}
.tabs button[aria-pressed="true"]{background:var(--ink);color:var(--page);border-color:var(--ink)}
details{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:10px 14px;margin:8px 0}
summary{cursor:pointer;font-weight:600}
.resp{margin:8px 0 4px;padding-left:12px;border-left:3px solid var(--bom)}
.resp.ruim{border-left-color:var(--ruim)}
.resp b{font-weight:650}
code{font-size:12px;background:var(--vazio);padding:1px 5px;border-radius:4px}
.nota{font-size:13px;color:var(--ink2);background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:10px 14px;margin:10px 0}
.escala{display:flex;align-items:center;gap:6px;font-size:12px;color:var(--muted);margin:8px 0}
.escala i{display:inline-block;width:26px;height:10px;border-radius:2px}
@media (max-width:640px){table{font-size:12px} th,td{padding:5px 4px} td.c{width:40px}}
</style>
</head>
<body>
<main>
<h1>Ragas × DeepEval × Promptfoo</h1>
<p>As mesmas 16 respostas (8 perguntas × 2 RAGs) avaliadas pelas três bibliotecas. Notas de 0 a 1. Quanto maior, melhor.</p>
<p class="sub" id="meta"></p>

<h2>1. Média das 8 perguntas</h2>
<p>Um gráfico por métrica. Em cada um, as três ferramentas lado a lado, com o RAG bom e o RAG ruim.</p>
<div class="legenda"><span><i class="sw" style="background:var(--bom)"></i>RAG bom (busca por embedding)</span><span><i class="sw" style="background:var(--ruim)"></i>RAG ruim (busca por palavras)</span></div>
<div class="grid" id="graficos"></div>

<h2>2. Nota por pergunta</h2>
<p>Cada célula é a nota de uma ferramenta em uma métrica. Passe o mouse para ler o motivo que o juiz deu (Ragas não devolve motivo).</p>
<div class="tabs" id="tabs"></div>
<div class="escala">0 <i style="background:var(--seq1)"></i><i style="background:var(--seq2)"></i><i style="background:var(--seq3)"></i><i style="background:var(--seq4)"></i><i style="background:var(--seq5)"></i><i style="background:var(--seq6)"></i> 1 &nbsp; <i style="background:var(--vazio)"></i> sem nota (erro do juiz)</div>
<div style="overflow-x:auto"><table id="tabela"></table></div>

<h2>3. O que cada RAG respondeu</h2>
<p>Pergunta, gabarito, trechos usados e resposta. Clique para abrir.</p>
<div id="respostas"></div>
</main>
<div class="tip" id="tip"></div>
<script id="dados" type="application/json">__DADOS__</script>
<script>
const D = JSON.parse(document.getElementById('dados').textContent);
const F = D.ferramentas, M = D.metricas;
const NOME = {ragas:'Ragas', deepeval:'DeepEval', promptfoo:'Promptfoo'};
const tip = document.getElementById('tip');
function mostrarTip(e, txt){ tip.textContent = txt; tip.style.display='block'; moverTip(e); }
function moverTip(e){ const w = tip.offsetWidth, h = tip.offsetHeight; let x = e.clientX+14, y = e.clientY+14;
  if (x+w > innerWidth-8) x = e.clientX-w-14; if (y+h > innerHeight-8) y = e.clientY-h-14; tip.style.left=x+'px'; tip.style.top=y+'px'; }
function esconderTip(){ tip.style.display='none'; }
const f2 = v => v==null ? '–' : v.toFixed(2);

document.getElementById('meta').textContent = `Gerado em ${D.gerado}. Juiz: ${[...new Set(Object.values(D.juiz))].join(' e ')} pelo endpoint OpenAI-compatível do Gemini (${F.map(f=>NOME[f]+': '+D.juiz[f]).join('; ')}).`;

// 1. gráficos de barras (um por métrica)
const G = document.getElementById('graficos');
for (const met of M){
  const W = 300, H = 190, pl = 28, pr = 8, pt = 10, pb = 28, iw = W-pl-pr, ih = H-pt-pb;
  const grupo = iw / F.length, bw = Math.min(24, grupo*0.3), gap = 2;
  let s = `<svg viewBox="0 0 ${W} ${H}" width="100%" role="img" aria-label="${D.rotulo[met]}, média por ferramenta">`;
  for (const t of [0,0.5,1]){ const y = pt + ih*(1-t); s += `<line class="${t===0?'ax':'gl'}" x1="${pl}" x2="${W-pr}" y1="${y}" y2="${y}"/><text class="tick" x="${pl-5}" y="${y+4}" text-anchor="end">${t}</text>`; }
  F.forEach((f,i)=>{
    const cx = pl + grupo*i + grupo/2;
    [['bom','--bom'],['ruim','--ruim']].forEach(([modo,cor],j)=>{
      const v = D.medias[`${f}|${modo}|${met}`];
      const x = cx - bw - gap/2 + j*(bw+gap);
      if (v==null){ s += `<text class="tick" x="${x+bw/2}" y="${pt+ih-4}" text-anchor="middle">–</text>`; return; }
      const h = Math.max(ih*v, 1), y = pt + ih - h, r = Math.min(4, h);
      const path = `M${x},${y+r} a${r},${r} 0 0 1 ${r},-${r} h${bw-2*r} a${r},${r} 0 0 1 ${r},${r} v${h-r} h-${bw} z`;
      s += `<path class="bar" d="${path}" fill="var(${cor})" data-tip="${NOME[f]} · RAG ${modo}\n${D.rotulo[met]}: ${f2(v)} (média de 8)"/>`;
      s += `<text class="val" x="${x+bw/2}" y="${y-3}" text-anchor="middle">${f2(v)}</text>`;
    });
    s += `<text x="${cx}" y="${H-9}" text-anchor="middle">${NOME[f]}</text>`;
  });
  s += '</svg>';
  G.insertAdjacentHTML('beforeend', `<div class="card"><h3>${D.rotulo[met]}</h3><p class="exp">${D.explica[met]}</p>${s}</div>`);
}
G.addEventListener('mouseover', e=>{ const b = e.target.closest('.bar'); if (b) mostrarTip(e, b.dataset.tip); });
G.addEventListener('mousemove', e=>{ if (tip.style.display==='block') moverTip(e); });
G.addEventListener('mouseout', e=>{ if (e.target.closest('.bar')) esconderTip(); });

// 2. tabela por pergunta
let modoAtual = 'bom';
const tabs = document.getElementById('tabs');
for (const modo of ['bom','ruim']){ tabs.insertAdjacentHTML('beforeend', `<button data-modo="${modo}" aria-pressed="${modo===modoAtual}">RAG ${modo}</button>`); }
tabs.addEventListener('click', e=>{ const b = e.target.closest('button'); if (!b) return; modoAtual = b.dataset.modo;
  tabs.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed', x.dataset.modo===modoAtual)); desenharTabela(); });
function corNota(v){ if (v==null) return ['var(--vazio)', true]; const i = Math.min(5, Math.floor(v*6)); return [`var(--seq${i+1})`, i < 2 && !matchMedia('(prefers-color-scheme: dark)').matches]; }
function desenharTabela(){
  const T = document.getElementById('tabela');
  let h = '<thead><tr><th rowspan="2">Pergunta</th>';
  for (const met of M) h += `<th class="g" colspan="${F.length}">${D.rotulo[met]}</th>`;
  h += '</tr><tr>';
  for (const met of M) F.forEach((f,i)=>{ h += `<th class="g" style="${i?'border-left:none':''}">${NOME[f]}</th>`; });
  h += '</tr></thead><tbody>';
  for (const p of D.perguntas){
    const m = p.modos[modoAtual];
    h += `<tr><td><b>${p.id}</b> ${p.pergunta}</td>`;
    for (const met of M) F.forEach((f,i)=>{
      const v = m.scores[f] ? m.scores[f][met] : null; const [cor, escuro] = corNota(v);
      const motivo = (m.motivos[f]||{})[met];
      const t = `${NOME[f]} · ${p.id} · RAG ${modoAtual}\n${D.rotulo[met]}: ${f2(v)}\n\n${motivo ? motivo : (f==='ragas' ? 'Ragas não devolve motivo, só a nota.' : 'Sem motivo registrado.')}`;
      h += `<td class="c ${i===0?'first':''}" data-tip="${t.replace(/"/g,'&quot;')}"><span class="${escuro?'escuro':''}" style="background:${cor}">${f2(v)}</span></td>`;
    });
    h += '</tr>';
  }
  T.innerHTML = h + '</tbody>';
}
desenharTabela();
const T = document.getElementById('tabela');
T.addEventListener('mouseover', e=>{ const c = e.target.closest('td.c'); if (c) mostrarTip(e, c.dataset.tip); });
T.addEventListener('mousemove', e=>{ if (tip.style.display==='block') moverTip(e); });
T.addEventListener('mouseout', e=>{ if (e.target.closest('td.c')) esconderTip(); });

// 3. respostas
const R = document.getElementById('respostas');
for (const p of D.perguntas){
  let h = `<details><summary>${p.id}. ${p.pergunta}</summary><p><b>Gabarito:</b> ${p.referencia}</p>`;
  for (const modo of ['bom','ruim']){ const m = p.modos[modo];
    h += `<div class="resp ${modo}"><b>RAG ${modo}</b> <span class="sub">(trechos ${m.contextos_ids.map(c=>`<code>${c}</code>`).join(' ')})</span><br>${m.resposta}</div>`; }
  R.insertAdjacentHTML('beforeend', h + '</details>');
}
</script>
</body>
</html>
"""


def main():
    dados, respostas = carregar()
    pacote = montar_dados(dados, respostas)
    html = HTML.replace("__DADOS__", json.dumps(pacote, ensure_ascii=False).replace("</", "<\\/"))
    destino = RAIZ / "docs" / "comparativo.html"
    destino.write_text(html, encoding="utf-8")
    print("gerado", destino, f"({len(html)//1024} KB, ferramentas: {', '.join(pacote['ferramentas'])})")


if __name__ == "__main__":
    main()
