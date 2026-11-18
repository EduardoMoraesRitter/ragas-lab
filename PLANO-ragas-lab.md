# PLANO ragas-lab

Objetivo: entender o Ragas na prática, comparando com DeepEval e Promptfoo sobre dois RAGs de brinquedo (busca boa e busca ruim) e um corpus com 3 fontes.

Aprovado pelo Eduardo em 18/11/2026.

## Checklist

- [ ] 1. Pasta, git e este PLANO
- [ ] 2. Ambiente: Python, Node, chave de LLM; conferir API atual de Ragas, DeepEval e Promptfoo (salvar em docs/pesquisa-apis.md)
- [ ] 3. Corpus com 3 fontes (manual, wiki, FAQ) + 8 perguntas com gabarito (corpus/, data/perguntas.json)
- [ ] 4. Dois RAGs de brinquedo (src/rag.py): busca boa e busca ruim; gerar respostas (data/respostas-*.json)
- [x] 5. Avaliar com Ragas (src/eval_ragas.py -> results/ragas.json). 16 linhas x 4 métricas, ~15 min no Gemini gratuito. Armadilha: ContextPrecision e ContextRecall recusam o campo `response`.
- [x] 6. Avaliar com DeepEval (src/eval_deepeval.py -> results/deepeval.json). 18 min, modo síncrono. OpenAIModel(base_url=...) funcionou com Gemini; custos por token precisaram ser passados.
- [ ] 7. Avaliar com Promptfoo (promptfooconfig.yaml -> results/promptfoo.json)
- [ ] 8. Relatório comparativo (docs/RELATORIO.md) e commit final

## Custo previsto

Cerca de 300 pedidos de LLM, abaixo de US$ 1 com modelo barato.
