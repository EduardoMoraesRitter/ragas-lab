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
| Repositório `ragas-lab` no GitHub | Criado em 19/11/2026, público |

## Checklist

- [x] 1. ragas-lab: README público (o que é, resultado, como rodar, aviso de dado fictício); tirar `results/promptfoo-view.log` do git
- [x] 2. ragas-lab: atualizar RELATORIO.md com as técnicas de busca (BM25, árvore, vetor, grafo, agêntica)
- [x] 3. Criar repositório público `EduardoMoraesRitter/ragas-lab` e fazer push. Feito em 19/11/2026: https://github.com/EduardoMoraesRitter/ragas-lab (commit 5127a95)
- [x] 4. Site: `src/data/ragas-lab/resultados.json` gerado por script a partir de `results/*.json` e `data/respostas-*.json`
- [x] 5. Site: página `src/pages/ragas-lab.astro` no estilo do Lab Pix: gráficos de barras por técnica, ranking, tabela por pergunta com motivo do juiz, link para o repositório
- [x] 6. Site: textos em `pt.json` e `en.json`; item "Lab RAG" no menu
- [x] 7. `npm run build` local sem erro; conferir a página em tema escuro, claro e em celular
- [x] 8. Commit no `main` do site, push, acompanhar o Actions, abrir a página no ar. Feito em 19/11/2026: commits d02bc1e e 8d8fe58, Actions verde, página no ar conferida no Chrome
- [x] 9. ragas-lab: `homepageUrl` do repositório apontando para a página do site. Feito na criação do repositório

## Decisões em aberto

- [x] Rodar DeepEval nas 4 técnicas novas antes de publicar: decidido pelo Eduardo em 18/11/2026. Juiz gemini-3.5-flash-lite, o mesmo das rodadas antigas do DeepEval.
- Nome no menu: "Lab RAG" (sugestão).

## Andamento (18/11/2026, 20h)

- Itens 1, 2, 4 a 7 prontos e commitados localmente. Nada publicado.
- Item 5: paleta dos avaliadores validada com validate_palette.js nos dois temas (a do Lab Pix falhava: azul-aço e lavanda quase iguais). Títulos curtos para não quebrar a linha do cabeçalho.
- Item 7: build sem erro; conferido no Chrome em tema escuro, claro, celular de 390 px (sem rolagem lateral) e em inglês.
- DeepEval nas técnicas novas: 1ª tentativa deu 429 em todas as chamadas (cota diária de 500 do gemini-3.5-flash-lite). Retomada agendada para 05:05 de 19/11, com o mesmo juiz. O script agora retoma só as notas vazias.
- Falta: DeepEval, reexportar os dados para o site, itens 3, 8 e 9.

## Andamento (19/11/2026, 05h)

- 2ª tentativa do DeepEval (05:05): 59 de 128 notas. As outras 69 deram 429 do limite por minuto, não do diário (uma chamada de teste às 05:15 passou).
- Correção: o script agora espera 40 s e tenta de novo até 4 vezes no 429. 3ª tentativa rodando com pausa de 5 s, só nas notas vazias.
- 3ª tentativa (05:15 a 05:31): 127 de 128 notas. 4ª tentativa refez a única nota com JSON inválido. DeepEval completo.
- Resultado mudou o topo: agêntica 0,92, árvore 0,91 (DeepEval prefere a agêntica, Ragas a árvore). Veredito do site, README e RELATORIO trocados para "empate no topo". Grafo fica abaixo do piso em cada avaliador sozinho; isso foi escrito no README e no RELATORIO.
- Menu do site: com 11 itens, passava da tela entre 769 e cerca de 1000 px. Aperto novo em `global.css` a partir de 1040 px; conferido de 769 a 1440 px.
- Tudo publicado em 19/11/2026.
