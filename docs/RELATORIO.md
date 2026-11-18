# Ragas na prática: comparado com DeepEval e Promptfoo

Data: 18/11/2026. Números completos em `docs/tabelas.md`. Página com gráficos: `docs/comparativo.html` (abrir no navegador).

## Resposta curta

1. **Ragas não é um RAG. É um juiz de RAG.** Ele recebe pergunta, trechos recuperados, resposta e gabarito, e devolve notas de 0 a 1. Quem faz a busca e a resposta é o seu sistema.
2. **As três ferramentas fazem a mesma coisa** com as mesmas 4 métricas. A diferença está no que vem junto: motivo da nota, interface, integração com testes.
3. **Ragas separou bem o RAG bom do RAG ruim** nas 4 métricas. DeepEval errou a relevância do RAG ruim (deu 0,96 para respostas que recusavam). Promptfoo: ver seção 5.
4. **O juiz manda mais do que a biblioteca.** Metade das discordâncias vem do modelo barato que julgou, não do código do Ragas ou do DeepEval.
5. **Nenhuma tem interface pronta e grátis que mostre tudo.** Só o Promptfoo tem painel local. A página `comparativo.html` deste projeto mostra as três lado a lado.

## 1. O que foi montado

| Peça | Onde | O que é |
|---|---|---|
| Corpus | `corpus/manual.md`, `wiki.md`, `faq.md` | 3 fontes fictícias sobre a cafeteira "Aurora K2", 10 trechos cada |
| Perguntas | `data/perguntas.json` | 8 perguntas com gabarito. A q8 é armadilha: pergunta sobre a K3, que não tem dado nas fontes |
| RAG bom | `src/rag.py buscar_bom` | busca por embedding (`gemini-embedding-001`), 3 trechos |
| RAG ruim | `src/rag.py buscar_ruim` | busca por palavras em comum, incluindo "a", "de", "o"; 2 trechos. Feito para errar |
| Respostas | `data/respostas-bom.json`, `respostas-ruim.json` | 16 respostas geradas pelo Gemini, com ordem de recusar quando o trecho não tem a resposta |
| Avaliação | `src/eval_ragas.py`, `src/eval_deepeval.py`, `src/promptfoo_config.py` | mesmas 16 respostas, mesmas 4 métricas, nas 3 ferramentas |
| Resultado | `results/*.json` | mesmo formato nos três: `modo`, `id`, `scores`, `detalhes` |

As 4 métricas, em português:

| Métrica | Pergunta que ela responde | Precisa de gabarito? |
|---|---|---|
| Fidelidade (faithfulness) | A resposta só diz o que está nos trechos recuperados? | Não |
| Relevância da resposta (answer relevancy) | A resposta fala do que foi perguntado? | Não |
| Precisão do contexto (context precision) | Os trechos recuperados são os certos? | Sim |
| Cobertura do contexto (context recall) | Os trechos cobrem o gabarito inteiro? | Sim |

Juiz: Gemini 3.5 Flash Lite (nível gratuito) para Ragas e DeepEval. Para o Promptfoo, Gemini 3.1 Flash Lite, porque a cota diária do 3.5 acabou (500 pedidos por dia). Isso é uma ressalva real: o juiz do Promptfoo não é o mesmo dos outros dois.

## 2. Resultado: média das 8 perguntas

| Ferramenta | RAG | Fidelidade | Relevância | Precisão ctx | Cobertura ctx |
|---|---|---|---|---|---|
| Ragas | bom | 0,98 | 0,80 | 0,50 | 0,88 |
| Ragas | ruim | 0,72 | 0,42 | 0,31 | 0,58 |
| DeepEval | bom | 0,88 | 0,96 | 0,77 | 0,81 |
| DeepEval | ruim | 0,50 | 0,96 | 0,50 | 0,42 |
| Promptfoo | bom | ver `tabelas.md` | | | |
| Promptfoo | ruim | ver `tabelas.md` | | | |

Leitura:

- **As três enxergam que o RAG ruim é pior** em fidelidade, precisão e cobertura. O experimento funcionou.
- **Relevância é onde elas brigam.** Ragas derruba o RAG ruim (0,42). DeepEval dá 0,96 para os dois. O motivo está na seção 3.
- **Precisão do contexto é baixa até no RAG bom** (0,50 no Ragas). O RAG bom traz 3 trechos e muitas vezes só 1 é útil. A métrica pune trecho útil fora da primeira posição.

## 3. Onde as ferramentas discordam, e por quê

### 3.1 A recusa: "Não encontrei essa informação nas fontes disponíveis."

Aparece em bom q8 e em ruim q3, q6, q7, q8. É o caso mais revelador.

| Métrica | Ragas | DeepEval | Quem tem razão |
|---|---|---|---|
| Fidelidade | 1,0 | 0,0 | Depende da definição. Ragas: a recusa não inventa nada, então é fiel. DeepEval: a recusa contradiz o contexto quando o contexto tinha a resposta. Na q8 (K3, sem dado) o DeepEval errou: deu 0,0 e escreveu que o contexto "fornece informação diversa sobre a K2", o que não responde sobre a K3. |
| Relevância | 0,0 | 1,0 | Ragas. A recusa não responde à pergunta. DeepEval considera que "não ter frase irrelevante" basta, e dá nota máxima para uma não-resposta. |

Consequência prática: **com DeepEval, um RAG que recusa tudo tira 1,0 em relevância.** Com Ragas, tira 0,0. Se o seu sistema recusa muito, a escolha da ferramenta muda a conclusão.

### 3.2 Erros do juiz, não da biblioteca

- DeepEval, bom q8, cobertura 0,0 e precisão 0,0: correto, não há dado da K3. Mas em fidelidade o juiz confundiu K2 com K3.
- DeepEval, ruim q5, precisão do contexto: "Evaluation LLM outputted an invalid JSON". O modelo barato não devolveu o JSON que a biblioteca pede. Fica sem nota.
- Ragas, bom q3, precisão 0,0 com cobertura 0,5: os trechos tinham a garantia de 12 meses, mas o juiz não marcou nenhum como útil. Ragas não devolve motivo, então não dá para saber o que ele pensou.

Lição: **a nota é tão boa quanto o modelo que julga.** Um juiz de nível gratuito gera ruído de 10 a 20 pontos. Para decisão séria, usar um modelo forte como juiz e rodar mais de uma vez.

### 3.3 Precisão do contexto: definições diferentes

Ragas e DeepEval calculam precisão com peso pela posição (o trecho útil tem que vir primeiro). Promptfoo não tem "context precision"; o mais perto é "context relevance" (quanto do contexto é relevante), sem olhar ordem. Os números dessa coluna **não são comparáveis** entre Promptfoo e os outros dois.

## 4. Ragas: o que faz de bom e de ruim

**De bom**

1. Métricas com definição publicada e usada como referência pelas outras ferramentas. "Faithfulness do Ragas" virou o nome padrão.
2. Decompõe a resposta em afirmações e checa uma a uma. Deu as notas mais coerentes com o que os olhos veem (seção 3.1).
3. Funciona com qualquer LLM pelo endpoint OpenAI: foi direto com o Gemini.
4. Tem métricas que as outras não têm (ou têm menos): fidelidade multimodal, avaliação de agentes e de ferramentas, geração de dataset de teste a partir dos documentos.
5. Nota contínua entre 0 e 1, com cálculo explícito (fração de afirmações sustentadas), não nota "no feeling" do juiz.

**De ruim**

1. **Não devolve motivo.** Só o número. Para investigar um 0,0 é preciso rodar o prompt na mão. DeepEval e Promptfoo trazem a explicação.
2. **API mudou muito.** Em 2026 a 0.4 tem a API nova `metrics.collections` com `ascore`, e a antiga `evaluate()` com `SingleTurnSample`. Tutoriais de 2024 não rodam. `ContextPrecision` recusa o campo `response`, por exemplo.
3. **Sem interface própria grátis.** O painel é o app.ragas.io, pago e hospedado.
4. **Sem prompt em português.** Os prompts do juiz são em inglês. Funcionou com conteúdo em português, mas o modelo barato tropeçou mais (ver 3.2).
5. **Lento com cota baixa**: 64 chamadas de juiz levaram 15 minutos no Gemini gratuito, por causa das pausas. Isso é do nível gratuito, não do Ragas, mas vale para as três.

## 5. Promptfoo e DeepEval em comparação

| | Ragas | DeepEval | Promptfoo |
|---|---|---|---|
| É o quê | biblioteca Python de métricas | framework de testes Python (estilo pytest) | ferramenta de linha de comando em Node, config em YAML |
| Motivo da nota | não | sim | sim |
| Interface | app.ragas.io (pago) | Confident AI (nuvem, login) | `promptfoo view` (local, grátis) |
| Encaixe | pipeline Python, notebooks | suíte de testes, CI | comparar prompts e modelos, CI, red team |
| Pegadinha vista aqui | API nova vs antiga; sem motivo | relevância 1,0 para recusa; juiz barato quebra o JSON | lista em `vars` vira N casos de teste (produto cartesiano); não tem precisão com ordem |
| Tempo (16 respostas, 4 métricas) | 15 min | 18 min | ver `tabelas.md` |

Promptfoo: resultado e tempo em `docs/tabelas.md`, seção 1, e na página `comparativo.html`.

## 6. Custo

Zero em dinheiro. Tudo rodou no nível gratuito do Gemini. O preço foi tempo: cerca de 1 hora de execução no total, por causa do limite de pedidos por minuto e por dia.

## 7. Quando usar qual

- **Quer só medir um RAG em Python e já tem pipeline**: Ragas. Aceitar que vai precisar ver o motivo na mão.
- **Quer testes que falham no CI e explicação de cada nota**: DeepEval. Conferir a definição de relevância antes de confiar.
- **Quer comparar prompts e modelos, com painel local grátis**: Promptfoo. Lembrar que as métricas de RAG são as mais simples das três.
- **Em qualquer caso**: juiz forte, mais de uma rodada, e uma amostra lida com os próprios olhos.

## 8. Como rodar de novo

```
.venv\Scripts\python src\rag.py ambos
.venv\Scripts\python src\eval_ragas.py
.venv\Scripts\python src\eval_deepeval.py
.venv\Scripts\python src\promptfoo_config.py gerar
npx promptfoo eval -c promptfooconfig.yaml --env-file .env --output results\promptfoo-raw.json --no-cache --max-concurrency 1
.venv\Scripts\python src\promptfoo_config.py converter
.venv\Scripts\python src\relatorio.py
.venv\Scripts\python src\pagina.py
```

Chave e modelos ficam em `.env` (não versionado). `PAUSA_S` controla a pausa entre chamadas.
