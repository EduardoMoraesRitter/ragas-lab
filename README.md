# ragas-lab

Qual técnica de busca traz o trecho certo num RAG? E as ferramentas de avaliação concordam entre si?

Este laboratório roda o mesmo RAG com 6 técnicas de busca e mede o resultado com três avaliadores: [Ragas](https://docs.ragas.io), [DeepEval](https://deepeval.com/docs) e [Promptfoo](https://www.promptfoo.dev/docs).

**Página com gráficos e todas as respostas:** https://eduardomoraesritter.github.io/ragas-lab/

## Resultado

Nota da busca = média de precisão e cobertura do contexto. Precisão diz se os trechos trazidos são os certos. Cobertura diz se eles contêm tudo o que o gabarito pede.

| Posição | Técnica | Como busca | LLM na busca, por pergunta |
|---|---|---|---|
| 1 | Árvore (estilo PageIndex) | O LLM lê um sumário com título e resumo de cada seção e escolhe a seção | 1 |
| 2 | Agêntica | O LLM busca sozinho com listar, grep e ler, em até 6 passos | 2 a 7 |
| 3 | Vetor | Embedding e os 3 trechos mais parecidos | 0 |
| 4 | BM25 | Palavra exata, sem stopwords | 0 |
| 5 | Grafo (GraphRAG) | Grafo em memória com networkx, sem Neo4j; anda 1 salto a partir das entidades da pergunta | 0 |
| 6 | Palavras (piso) | Conta palavras em comum, inclusive "a" e "de". Feita para errar | 0 |

Números completos em [docs/RELATORIO.md](docs/RELATORIO.md) e [docs/tabelas.md](docs/tabelas.md).

O que se aprende:

1. **Ragas não é um RAG. É um juiz de RAG.** Ele recebe pergunta, trechos, resposta e gabarito, e devolve notas de 0 a 1.
2. **Precisão e cobertura do contexto medem a busca.** Fidelidade e relevância medem a resposta. Com as quatro dá para dizer se o problema está no banco de vetores ou no LLM.
3. **Os avaliadores discordam na recusa.** Para a resposta "não encontrei", o Ragas dá relevância 0,0 e o DeepEval dá 1,0.
4. **O juiz pesa mais que a biblioteca.** Um juiz de nível gratuito gera ruído de 10 a 20 pontos e às vezes sai do formato.

## Dados

O corpus é **fictício**: a cafeteira "Aurora K2", da empresa inventada "Caffeo Brasil", em 3 fontes (manual, wiki e FAQ) com 10 seções cada. São 8 perguntas com gabarito. Uma delas é armadilha: pergunta sobre um modelo que não existe nas fontes.

Inventado de propósito: o juiz não pode responder de memória, e o gabarito é exato. Limite: 8 perguntas e 30 trechos servem para entender as técnicas, não para ranquear RAGs reais.

## Como rodar

Se estiver no Windows, troque `.venv/bin/` por `.venv\Scripts\` nos comandos.

1. Crie o ambiente e instale as bibliotecas:

   ```
   python -m venv .venv
   .venv/bin/pip install -r requirements.txt
   ```

2. Copie `.env.example` para `.env` e coloque a sua chave. Qualquer API compatível com OpenAI serve.

3. Gere as respostas de cada técnica:

   ```
   .venv/bin/python src/rag.py todas
   ```

4. Avalie. A variável `TECNICAS` escolhe as técnicas; sem ela, roda vetor e piso:

   ```
   TECNICAS=bom,ruim,bm25,arvore,agentico,grafo .venv/bin/python src/eval_ragas.py
   TECNICAS=bom,ruim,bm25,arvore,agentico,grafo .venv/bin/python src/eval_deepeval.py
   .venv/bin/python src/promptfoo_config.py gerar
   npx promptfoo eval -c promptfooconfig.yaml --env-file .env --output results/promptfoo-raw.json --no-cache
   .venv/bin/python src/promptfoo_config.py converter
   ```

5. Gere as tabelas e a página local:

   ```
   .venv/bin/python src/relatorio.py
   .venv/bin/python src/pagina.py
   ```

O nível gratuito do Gemini aceita 500 pedidos por dia por modelo. Uma rodada completa passa disso; o DeepEval retoma de onde parou se o arquivo de resultado já existir.

## Estrutura

| Pasta | O que tem |
|---|---|
| `corpus/` | As 3 fontes fictícias |
| `data/` | Perguntas, respostas de cada técnica, índice da árvore, triplas do grafo e cache de embeddings |
| `src/` | RAG (`rag.py`), avaliadores, tabelas, página local e exportação para o site |
| `results/` | Notas e motivos de cada avaliador |
| `docs/` | Relatório, tabelas, pesquisa das APIs (novembro de 2026) e página local |
