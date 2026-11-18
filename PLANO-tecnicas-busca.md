# PLANO: comparar técnicas de busca com Ragas, DeepEval e Promptfoo

Objetivo: trocar só a etapa de busca (retrieval), manter corpus, perguntas, gerador e juiz, e ver qual técnica traz os trechos certos. As métricas de busca são precisão do contexto e cobertura do contexto. Fidelidade e relevância ficam como controle.

Origem das técnicas: notas do Obsidian "RAG - Técnicas Modernas e Vectorless (2026)" e "LangChain e RAG" (seções Retrieval e RAG Avançado). Proposto em 18/11/2026, aguardando ok do Eduardo.

## Técnicas (uma função `buscar_<nome>` em src/rag.py cada)

| # | Técnica | Da nota | Custo por pergunta | Observação |
|---|---|---|---|---|
| 1 | Palavras (ruim) | base | 0 chamadas | já existe; é o piso |
| 2 | BM25 | "Keyword / BM25" | 0 | o "velho que voltou"; biblioteca rank_bm25 |
| 3 | Vetor (embedding) | "Vector search" | 0 (cache) | já existe, era o "bom" |
| 4 | Híbrido BM25 + vetor | "Hybrid search" | 0 | fusão RRF |
| 5 | Híbrido + rerank por LLM | "Hybrid + Rerank" | 1 | padrão de produção 2026 segundo a nota |
| 6 | Multi-query | "Multi-query" | 1 | LLM gera 3 variações da pergunta, busca vetor em cada |
| 7 | HyDE | "HyDE" | 1 | LLM escreve resposta hipotética, busca por ela |
| 8 | Pai-filho | "Parent-child retrieval" | 0 | chunk pequeno acha, devolve a seção inteira |
| 9 | Árvore (PageIndex) | "PageIndex / vectorless" | 1 a 2 | índice: título e resumo por seção (uma vez); consulta: LLM escolhe os nós |
| 10 | Agêntico | "Agentic retrieval" | 3 a 5 | LLM com ferramentas listar/ler/grep no corpus, até 5 passos |
| 11 | GraphRAG | "GraphRAG / Neo4j" | 1 a 2 | opcional, fase 2: extrair entidades e relações do corpus (networkx em memória) |

## Checklist

- [ ] 1. Ampliar perguntas de 8 para 20 (gabarito escrito à mão, custo 0). 8 é pouco para ordenar 10 técnicas.
- [ ] 2. Refatorar src/rag.py: registro de técnicas, `python src/rag.py <tecnica>` gera data/respostas-<tecnica>.json
- [ ] 3. Técnicas sem LLM: BM25, híbrido, pai-filho (itens 2, 4, 8)
- [ ] 4. Técnicas com 1 chamada: rerank, multi-query, HyDE (5, 6, 7)
- [ ] 5. Árvore PageIndex (9): indexação com resumo por seção + consulta por raciocínio
- [ ] 6. Agêntico (10)
- [ ] 7. Avaliadores aceitam `--tecnica` e gravam results/<ferramenta>-<tecnica>.json
- [ ] 8. Rodada de varredura: todas as técnicas só com Ragas (mais barato, ~5 chamadas por caso)
- [ ] 9. Rodada final: as 3 melhores e a pior com as 3 ferramentas
- [ ] 10. Página comparativo.html ganha eixo "técnica"; relatório e nota no Obsidian
- [ ] 11. GraphRAG (opcional, só se os itens anteriores fecharem)

## Custo

Chamadas de juiz por técnica, 20 perguntas: Ragas ~100, DeepEval ~180, Promptfoo ~140.

- Varredura (10 técnicas × Ragas): ~1.000 chamadas + ~100 de geração + ~150 das técnicas com LLM.
- Final (4 técnicas × 3 ferramentas): ~1.700 chamadas.
- Total: ~3.000 chamadas.

Nível gratuito do Gemini: 500 por dia por modelo no flash-lite. Dá para fazer em 3 a 4 dias alternando modelos, ou em 1 tarde com chave paga (flash-lite custa cerca de US$ 0,10 por milhão de tokens de entrada; estimativa total abaixo de US$ 1).

## Decisões em aberto (Eduardo)

- Chave paga ou nível gratuito espalhado em dias?
- Incluir GraphRAG (item 11) ou deixar para depois?
- 20 perguntas está bom, ou quer mais?
