# PLANO: publicar o ragas-lab no GitHub e no portfólio

Pedido do Eduardo em 18/11/2026: melhorar o design no estilo do site, publicar o repositório como público e ligar ao portfólio. Verificação feita antes de executar; aguardando ok.

## O que foi verificado (18/11/2026)

| Item | Resultado |
|---|---|
| Acesso ao GitHub | `gh` logado na conta EduardoMoraesRitter |
| Repositório do site | `Projetos/eduardomoraesritter.github.io` (o antigo `MeuSite` é o mesmo repositório, renomeado). Público. Atualizado com `git pull` (estava 27 commits atrás) |
| Como o site sobe | Astro 5. Push no `main` dispara GitHub Actions, que gera `dist/` e publica em https://eduardomoraesritter.github.io |
| Modelo de página extra | "Lab Pix" em `src/pages/pix-golpe.astro`: usa `Nav`, `Footer`, `global.css`; dados em `src/data/pix-golpe/corrida.json`; textos em `src/i18n/pt.json` e `en.json`; link no menu em `src/components/Nav.astro` |
| Design do site | Escuro por padrão, com tema claro. Fundo `#080808`, destaque dourado `#c9a96e`. Títulos em Google Sans Display e Cormorant Garamond itálico; texto em Outfit. Pontilhado de fundo, etiquetas em caixa com borda fina, letras espaçadas em maiúsculas |
| Design da página atual do ragas-lab | `docs/comparativo.html`: página solta, fonte do sistema, paleta azul/laranja/verde. Não combina com o site |
| ragas-lab pode ficar público? | Sim. `.env` nunca foi commitado; nenhuma chave `AIza` em nenhum commit; autor dos commits só `eduardo.moraes.ritter@gmail.com`; corpus é fictício. Repositório com 2,6 MB |
| Repositório `ragas-lab` no GitHub | Não existe ainda |

## Checklist

- [ ] 1. ragas-lab: README público (o que é, resultado, como rodar, aviso de dado fictício); tirar `results/promptfoo-view.log` do git
- [ ] 2. ragas-lab: atualizar RELATORIO.md com as técnicas de busca (BM25, árvore, vetor, grafo, agêntica)
- [ ] 3. Criar repositório público `EduardoMoraesRitter/ragas-lab` e fazer push
- [ ] 4. Site: `src/data/ragas-lab/resultados.json` gerado por script a partir de `results/*.json` e `data/respostas-*.json`
- [ ] 5. Site: página `src/pages/ragas-lab.astro` no estilo do Lab Pix: gráficos de barras por técnica, ranking, tabela por pergunta com motivo do juiz, link para o repositório
- [ ] 6. Site: textos em `pt.json` e `en.json`; item "Lab RAG" no menu
- [ ] 7. `npm run build` local sem erro; conferir a página em tema escuro, claro e em celular
- [ ] 8. Commit no `main` do site, push, acompanhar o Actions, abrir a página no ar
- [ ] 9. ragas-lab: `homepageUrl` do repositório apontando para a página do site

## Decisões em aberto

- Rodar DeepEval e Promptfoo nas 4 técnicas novas antes de publicar? Sem isso, a página mostra essas técnicas só com Ragas.
- Nome no menu: "Lab RAG" (sugestão).
