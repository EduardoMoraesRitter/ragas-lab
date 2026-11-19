# Tabelas geradas (src/relatorio.py)

## 1. Média por ferramenta e por técnica de busca

| Ferramenta | Técnica | Fidelidade | Relevância da resposta | Precisão do contexto | Cobertura do contexto |
|---|---|---|---|---|---|
| ragas | palavras (ruim) | 0.72 | 0.42 | 0.31 | 0.58 |
| ragas | vetor (bom) | 0.98 | 0.80 | 0.50 | 0.88 |
| ragas | BM25 | 1.00 | 0.57 | 0.50 | 0.71 |
| ragas | árvore | 0.79 | 0.78 | 0.88 | 0.92 |
| ragas | agêntico | 0.88 | 0.78 | 0.88 | 0.85 |
| ragas | grafo | 1.00 | 0.34 | 0.31 | 0.46 |
| deepeval | palavras (ruim) | 0.50 | 0.96 | 0.50 | 0.42 |
| deepeval | vetor (bom) | 0.88 | 0.96 | 0.77 | 0.81 |
| deepeval | BM25 | 0.65 | 0.94 | 0.75 | 0.62 |
| deepeval | árvore | 0.88 | 1.00 | 0.94 | 0.92 |
| deepeval | agêntico | 0.88 | 1.00 | 1.00 | 0.94 |
| deepeval | grafo | 0.62 | 1.00 | 0.54 | 0.35 |
| promptfoo | palavras (ruim) | 0.83 | 0.65 | 0.17 | 0.37 |
| promptfoo | vetor (bom) | 1.00 | 0.85 | 0.25 | 0.78 |

## 2. Fidelidade por pergunta (palavras (ruim) / vetor (bom) / BM25 / árvore / agêntico / grafo)

| Pergunta | ragas | deepeval | promptfoo |
|---|---|---|---|
| q1 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / – / – / – / – |
| q2 | 0.75 / 1.00 / 1.00 / 0.33 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / – / – / – / – |
| q3 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 0.00 / 1.00 / 1.00 / 1.00 / 1.00 / 0.00 | 1.00 / 1.00 / – / – / – / – |
| q4 | 1.00 / 1.00 / 1.00 / 0.00 / 0.00 / 1.00 | 1.00 / 1.00 / 0.00 / 1.00 / 1.00 / 0.00 | 0.67 / 1.00 / – / – / – / – |
| q5 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / – / – / – / – |
| q6 | 0.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 0.00 / 1.00 / 0.67 / 1.00 / 1.00 / 1.00 | 0.00 / 1.00 / – / – / – / – |
| q7 | 0.00 / 0.83 / 1.00 / 1.00 / 1.00 / 1.00 | 0.00 / 1.00 / 0.50 / 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / – / – / – / – |
| q8 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 | 1.00 / 1.00 / – / – / – / – |

## 2. Relevância da resposta por pergunta (palavras (ruim) / vetor (bom) / BM25 / árvore / agêntico / grafo)

| Pergunta | ragas | deepeval | promptfoo |
|---|---|---|---|
| q1 | 0.99 / 0.95 / 0.00 / 0.85 / 0.85 / 0.00 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 0.96 / 0.95 / – / – / – / – |
| q2 | 0.81 / 0.77 / 0.81 / 0.81 / 0.81 / 0.76 | 0.67 / 0.67 / 0.50 / 1.00 / 1.00 / 1.00 | 0.80 / 0.74 / – / – / – / – |
| q3 | 0.00 / 0.97 / 0.99 / 0.96 / 0.99 / 0.00 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 0.48 / 0.97 / – / – / – / – |
| q4 | 0.70 / 0.98 / 0.00 / 0.98 / 0.98 / 0.00 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 0.68 / 0.98 / – / – / – / – |
| q5 | 0.88 / 0.87 / 1.00 / 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 0.86 / 0.85 / – / – / – / – |
| q6 | 0.00 / 0.88 / 0.74 / 0.62 / 0.62 / 0.00 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 0.47 / 0.86 / – / – / – / – |
| q7 | 0.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 0.47 / 1.00 / – / – / – / – |
| q8 | 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 0.48 / 0.48 / – / – / – / – |

## 2. Precisão do contexto por pergunta (palavras (ruim) / vetor (bom) / BM25 / árvore / agêntico / grafo)

| Pergunta | ragas | deepeval | promptfoo |
|---|---|---|---|
| q1 | 0.00 / 0.33 / 0.00 / 1.00 / 1.00 / 0.00 | 1.00 / 1.00 / 0.50 / 1.00 / 1.00 / 1.00 | 0.67 / 0.60 / – / – / – / – |
| q2 | 1.00 / 1.00 / 1.00 / 0.50 / 1.00 / 0.00 | 1.00 / 1.00 / 1.00 / 0.50 / 1.00 / 0.83 | 0.00 / 0.20 / – / – / – / – |
| q3 | 0.00 / 0.00 / 0.00 / 0.50 / 0.00 / 0.00 | 0.00 / 1.00 / 0.50 / 1.00 / 1.00 / 0.00 | 0.00 / 0.00 / – / – / – / – |
| q4 | 0.50 / 0.33 / 0.00 / 1.00 / 1.00 / 0.00 | 0.50 / 0.33 / 0.00 / 1.00 / 1.00 / 0.00 | 0.33 / 0.20 / – / – / – / – |
| q5 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 0.50 | – / 1.00 / 1.00 / 1.00 / 1.00 / 0.50 | 0.33 / 0.20 / – / – / – / – |
| q6 | 0.00 / 0.33 / 0.00 / 1.00 / 1.00 / 1.00 | 1.00 / 0.83 / 1.00 / 1.00 / 1.00 / 1.00 | 0.00 / 0.40 / – / – / – / – |
| q7 | 0.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 0.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 0.00 / 0.40 / – / – / – / – |
| q8 | 0.00 / 0.00 / 1.00 / 1.00 / 1.00 / 0.00 | 0.00 / 0.00 / 1.00 / 1.00 / 1.00 / 0.00 | 0.00 / 0.00 / – / – / – / – |

## 2. Cobertura do contexto por pergunta (palavras (ruim) / vetor (bom) / BM25 / árvore / agêntico / grafo)

| Pergunta | ragas | deepeval | promptfoo |
|---|---|---|---|
| q1 | 0.50 / 1.00 / 0.50 / 1.00 / 1.00 / 0.50 | 0.00 / 1.00 / 0.00 / 1.00 / 1.00 / 0.00 | 0.50 / 1.00 / – / – / – / – |
| q2 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 0.00 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 0.00 | – / – / – / – / – / – |
| q3 | 0.00 / 0.50 / 0.50 / 1.00 / 0.50 / 0.00 | 0.00 / 0.50 / 0.50 / 1.00 / 0.50 / 0.00 | 0.00 / 0.50 / – / – / – / – |
| q4 | 1.00 / 1.00 / 0.00 / 1.00 / 1.00 / 0.00 | 1.00 / 1.00 / 0.00 / 1.00 / 1.00 / 0.00 | – / 1.00 / – / – / – / – |
| q5 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 / 1.00 / 1.00 / 1.00 | 1.00 / – / – / – / – / – |
| q6 | 0.67 / 1.00 / 0.67 / 1.00 / 1.00 / 0.67 | 0.33 / 1.00 / 0.50 / 1.00 / 1.00 / 0.33 | 0.33 / 0.67 / – / – / – / – |
| q7 | 0.00 / 1.00 / 1.00 / 0.33 / 0.33 / 1.00 | 0.00 / 1.00 / 1.00 / 0.33 / 1.00 / 1.00 | – / 1.00 / – / – / – / – |
| q8 | 0.50 / 0.50 / 1.00 / 1.00 / 1.00 / 0.50 | 0.00 / 0.00 / 1.00 / 1.00 / 1.00 / 0.50 | 0.00 / 0.50 / – / – / – / – |

## 3. O que cada RAG respondeu

### q1. Qual é a pressão da bomba da Aurora K2 e quanto ela pesa?

Gabarito: A bomba da Aurora K2 é de 15 bar e a máquina pesa 4,2 kg.

- **palavras (ruim)** (trechos wiki-05, faq-10): A pressão da bomba da Aurora K2 é de 15 bar. Não encontrei essa informação nas fontes disponíveis sobre o peso dela.
- **vetor (bom)** (trechos wiki-05, faq-10, manual-01): A cafeteira Aurora K2 possui uma bomba de 15 bar. O peso do aparelho é de 4,2 kg.
- **BM25** (trechos manual-09, wiki-05, faq-10): A Aurora K2 possui uma bomba de 15 bar. Não encontrei essa informação nas fontes disponíveis sobre o peso do equipamento.
- **árvore** (trechos manual-01): A Aurora K2 possui uma bomba de 15 bar e pesa 4,2 kg.
- **agêntico** (trechos manual-01): A Aurora K2 possui uma bomba de 15 bar e pesa 4,2 kg.
- **grafo** (trechos faq-10, manual-09, wiki-04): A Aurora K2 possui uma bomba de 15 bar. Não encontrei essa informação nas fontes disponíveis sobre o peso do equipamento.

### q2. A cada quantas extrações devo descalcificar a Aurora K2 se a água da minha cidade for dura?

Gabarito: Com água dura, a recomendação é descalcificar a cada 150 extrações, em vez das 300 do manual.

- **palavras (ruim)** (trechos faq-07, manual-04): Se a água da sua cidade for dura, recomendamos descalcificar a cada 150 extrações em vez de 300. Água dura acelera o acúmulo de calcário, e danos por calcário não são cobertos pela garantia.
- **vetor (bom)** (trechos faq-07, manual-04, wiki-05): Água dura acelera o acúmulo de calcário e recomendamos usar água filtrada e descalcificar a cada 150 extrações em vez de 300.
- **BM25** (trechos faq-07, manual-04, manual-06): Se a água da sua cidade for dura, recomendamos descalcificar a cada 150 extrações em vez de 300.
- **árvore** (trechos manual-04, faq-07): Se a água da sua cidade for dura, recomendamos descalcificar a cada 150 extrações em vez de 300.
- **agêntico** (trechos faq-07, manual-04): Recomendamos descalcificar a cada 150 extrações em vez de 300 se a água da sua cidade for dura. Isso ocorre porque a água dura acelera o acúmulo de calcário.
- **grafo** (trechos manual-04, wiki-04, manual-06): Descalcifique a cada 300 extrações ou quando a luz indicadora piscar em vermelho. A garantia não cobre danos por obstrução por água com alto teor de calcário.

### q3. Quanto tempo de garantia eu tenho na Aurora K2?

Gabarito: A garantia padrão é de 12 meses. Quem cadastra a máquina no site em até 30 dias ganha mais 12 meses, totalizando 24 meses.

- **palavras (ruim)** (trechos manual-01, wiki-05): Não encontrei essa informação nas fontes disponíveis.
- **vetor (bom)** (trechos manual-06, faq-02, faq-05): A Aurora K2 tem garantia legal e contratual de 12 meses contra defeitos de fabricação, contados a partir da data da nota fiscal.
- **BM25** (trechos faq-02, manual-06, manual-08): A Aurora K2 tem garantia legal e contratual de 12 meses contra defeitos de fabricação, contados a partir da data da nota fiscal.
- **árvore** (trechos manual-06, faq-04): A Aurora K2 possui garantia legal e contratual de 12 meses contra defeitos de fabricação. Ao cadastrar a máquina no site da Caffeo em até 30 dias após a compra, você ganha 12 meses adicionais, totalizando 24 meses de garantia.
- **agêntico** (trechos manual-06): A Aurora K2 tem garantia legal e contratual de 12 meses contra defeitos de fabricação, contados a partir da data da nota fiscal.
- **grafo** (trechos wiki-04, manual-04, wiki-09): Não encontrei essa informação nas fontes disponíveis.

### q4. Quem fundou a Caffeo Brasil e quem a preside hoje?

Gabarito: A Caffeo Brasil foi fundada por Helena Brandt e Rogério Tancredi. Helena Brandt é a presidente desde a fundação.

- **palavras (ruim)** (trechos faq-04, wiki-02): A empresa foi fundada por Helena Brandt e Rogério Tancredi. Helena Brandt é a presidente desde a fundação.
- **vetor (bom)** (trechos wiki-01, faq-08, wiki-02): A Caffeo Brasil foi fundada por Helena Brandt e Rogério Tancredi. Helena Brandt é a presidente desde a fundação.
- **BM25** (trechos faq-04, faq-08, wiki-01): Não encontrei essa informação nas fontes disponíveis.
- **árvore** (trechos wiki-02): A Caffeo Brasil foi fundada por Helena Brandt e Rogério Tancredi. Helena Brandt é a presidente desde a fundação.
- **agêntico** (trechos wiki-02): A Caffeo Brasil foi fundada por Helena Brandt e Rogério Tancredi. Helena Brandt é a presidente desde a fundação.
- **grafo** (trechos faq-04, wiki-06, wiki-07): Não encontrei essa informação nas fontes disponíveis.

### q5. Por que a Aurora K1 passou por recall e quantas unidades foram afetadas?

Gabarito: O recall de agosto de 2019 foi por falha no anel de vedação da caldeira, que podia vazar vapor. Foram 18.000 unidades.

- **palavras (ruim)** (trechos wiki-04, wiki-05): Em agosto de 2019, a Caffeo fez um recall voluntário da Aurora K1 devido a uma falha no anel de vedação da caldeira, que podia vazar vapor. No total, 18.000 unidades foram afetadas por esse problema.
- **vetor (bom)** (trechos wiki-04, wiki-03, faq-10): Em agosto de 2019, a Caffeo fez um recall voluntário da Aurora K1 devido a uma falha no anel de vedação da caldeira, que podia vazar vapor. O total de unidades afetadas foi de 18.000. Nenhum ferimento foi registrado em decorrência do problema.
- **BM25** (trechos wiki-04, wiki-05, wiki-03): A Aurora K1 passou por um recall devido a uma falha no anel de vedação da caldeira, que podia vazar vapor. Foram afetadas 18.000 unidades.
- **árvore** (trechos wiki-04): A Aurora K1 passou por um recall devido a uma falha no anel de vedação da caldeira, que podia vazar vapor. Foram afetadas 18.000 unidades.
- **agêntico** (trechos wiki-04): A Aurora K1 passou por um recall devido a uma falha no anel de vedação da caldeira, que podia vazar vapor. Foram afetadas 18.000 unidades.
- **grafo** (trechos wiki-05, wiki-04, manual-04): A Aurora K1 passou por um recall devido a uma falha no anel de vedação da caldeira, que podia vazar vapor. Foram afetadas 18.000 unidades.

### q6. Posso usar vinagre para descalcificar e a máquina aceita cápsulas?

Gabarito: Não aos dois. Vinagre danifica a vedação de silicone da caldeira. A máquina só funciona com café moído e não existe adaptador oficial para cápsulas.

- **palavras (ruim)** (trechos faq-02, wiki-02): Não encontrei essa informação nas fontes disponíveis.
- **vetor (bom)** (trechos manual-04, faq-01, faq-02): Não, você nunca deve usar vinagre para descalcificar, pois ele danifica a vedação de silicone da caldeira. Além disso, a Aurora K2 funciona apenas com café moído e não aceita cápsulas.
- **BM25** (trechos faq-02, faq-07, faq-09): Não encontrei essa informação nas fontes disponíveis. A Aurora K2 funciona apenas com café moído e não existe adaptador oficial para cápsulas.
- **árvore** (trechos manual-04, faq-02): Nunca use vinagre, pois ele danifica a vedação de silicone da caldeira. A Aurora K2 funciona apenas com café moído e não aceita cápsulas.
- **agêntico** (trechos manual-04, faq-02): Nunca use vinagre, pois ele danifica a vedação de silicone da caldeira. A Aurora K2 funciona apenas com café moído e não aceita cápsulas.
- **grafo** (trechos manual-04, manual-05, manual-06): Nunca use vinagre, pois ele danifica a vedação de silicone da caldeira. Não encontrei essa informação nas fontes disponíveis sobre a aceitação de cápsulas.

### q7. O que significa o código de erro E2 e como resolver?

Gabarito: E2 é pressão insuficiente. A causa comum é moagem grossa demais. A solução é usar moagem fina, parecida com açúcar refinado.

- **palavras (ruim)** (trechos manual-01, manual-03): Não encontrei essa informação nas fontes disponíveis.
- **vetor (bom)** (trechos manual-09, faq-06, faq-01): O código de erro E2 significa pressão insuficiente causada por moagem grossa demais, que deixa o café aguado. Para resolver, verifique a moagem e utilize uma moagem fina, parecida com açúcar refinado, evitando que seja grossa demais.
- **BM25** (trechos faq-06, manual-09, faq-01): O código de erro E2 significa pressão insuficiente. Para resolver, verifique a moagem, utilizando uma moagem fina, parecida com açúcar refinado.
- **árvore** (trechos manual-09): O código de erro E2 significa pressão insuficiente. Para resolver, verifique a moagem.
- **agêntico** (trechos manual-09): O código de erro E2 significa pressão insuficiente. Para resolver, verifique a moagem.
- **grafo** (trechos manual-09, faq-06): O código de erro E2 significa pressão insuficiente. Para resolver, verifique a moagem, pois uma moagem grossa demais causa esse erro.

### q8. Qual é a capacidade do reservatório de água da Aurora K3?

Gabarito: Não há essa informação. A Aurora K3 foi anunciada para 2027 e nenhuma especificação foi divulgada.

- **palavras (ruim)** (trechos faq-10, manual-01): Não encontrei essa informação nas fontes disponíveis.
- **vetor (bom)** (trechos wiki-05, faq-10, manual-01): Não encontrei essa informação nas fontes disponíveis.
- **BM25** (trechos wiki-09, manual-05, manual-01): Não encontrei essa informação nas fontes disponíveis.
- **árvore** (trechos wiki-09): Não encontrei essa informação nas fontes disponíveis.
- **agêntico** (trechos wiki-09): Não encontrei essa informação nas fontes disponíveis.
- **grafo** (trechos faq-10, wiki-04, faq-07): Não encontrei essa informação nas fontes disponíveis.

## 4. Motivos dados pelo juiz (DeepEval e Promptfoo devolvem; Ragas não)

- deepeval / ruim / q1 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with zero contradictions!
- deepeval / ruim / q1 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses all parts of the input regarding the Aurora K2's pump pressure and weight without including any irrelevant information. Great job!
- deepeval / ruim / q1 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts is relevant, as it directly provides the pressure of the Aurora K2 pump by stating 'bomba de 15 bar' ('It directly provides the pressure of the Aurora K2 pump by stating 'bomba de 15 bar'.'), and it is correctly ranked above the second node in the retrieval contexts, which is irrelevant because it discusses differences between K1 a
- deepeval / ruim / q1 / Cobertura do contexto = 0.00: The score is 0.00 because, although the first part of the sentence regarding the 15-bar pump of the Aurora K2 is found in the 1st and 2nd node(s) in retrieval context, the claim that the machine weighs 4.2 kg is entirely missing from all retrieval contexts.
- deepeval / ruim / q2 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / ruim / q2 / Relevância da resposta = 0.67: The score is 0.67 because while it correctly addresses the machine and water hardness mentioned in the input, it includes irrelevant information about warranty coverage instead of focusing solely on the descaling frequency.
- deepeval / ruim / q2 / Precisão do contexto = 1.00: The score is 1.00 because all relevant nodes containing the necessary information about descaling frequency for hard water were retrieved and perfectly prioritized!
- deepeval / ruim / q2 / Cobertura do contexto = 1.00: The score is 1.00 because all information in the expected output is fully supported by node(s) in the retrieval context. Fantastic job!
- deepeval / ruim / q3 / Fidelidade = 0.00: The score is 0.00 because the actual output claims that the information was not found, whereas the retrieval context actually provides complete details about the Aurora K2 coffee maker.
- deepeval / ruim / q3 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses the user's question about the warranty period without any irrelevant information.
- deepeval / ruim / q3 / Precisão do contexto = 0.00: The score is 0.00 because all retrieved nodes are irrelevant to the input. Specifically, the first node in the retrieval contexts is irrelevant because "The context mentions technical specifications like 'bomba de 15 bar' and dimensions, but does not provide any information regarding warranty," and the second node in the retrieval contexts is also irrelevant because "The context discusses the laun
- deepeval / ruim / q3 / Cobertura do contexto = 0.00: The score is 0.00 because the first sentence regarding the 12-month standard warranty and the second sentence about the warranty extension upon registration cannot be found in any of the nodes in the retrieval context.
- deepeval / ruim / q4 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / ruim / q4 / Relevância da resposta = 1.00: The score is 1.00 because the response directly and completely answers both parts of the input question without any irrelevant information.
- deepeval / ruim / q4 / Precisão do contexto = 0.50: The score is 0.50 because the first node in retrieval contexts is irrelevant, as "O texto fala sobre 'Como estender a garantia?' e cadastro da máquina no site, o que não tem relação com os fundadores ou a presidência da Caffeo Brasil.", and should be ranked lower than the second node, which is relevant because "O texto afirma diretamente que 'A empresa foi fundada por Helena Brandt e Rogério Tancr
- deepeval / ruim / q4 / Cobertura do contexto = 1.00: The score is 1.00 because all sentences in the expected output are fully supported by the information provided in the 2nd node in the retrieval context. Fantastic job!
- deepeval / ruim / q5 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions detected. Great job!
- deepeval / ruim / q5 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses all parts of the input question without including any irrelevant information.
- deepeval / ruim / q5 / Precisão do contexto = –: ERRO: DeepEvalError: Evaluation LLM outputted an invalid JSON. Please use a better evaluation model.
- deepeval / ruim / q5 / Cobertura do contexto = 1.00: The score is 1.00 because all sentences in the expected output are fully supported by the 1st node in the retrieval context. Fantastic job!
- deepeval / ruim / q6 / Fidelidade = 0.00: The score is 0.00 because the actual output incorrectly states that no information was found, whereas the context actually contains specific details about the Aurora K2 coffee maker and its founders.
- deepeval / ruim / q6 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and accurately addresses both parts of the user's input regarding using vinegar for descaling and the machine's capsule compatibility, with zero irrelevant statements.
- deepeval / ruim / q6 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts is relevant, stating that the machine 'funciona apenas com café moído' and 'Não existe adaptador oficial para cápsulas', while the second node discusses the founders and directors of the company ('Helena Brandt e Rogério Tancredi'), which is completely irrelevant to descaling the machine with vinegar, and it was correctly ranked lo
- deepeval / ruim / q6 / Cobertura do contexto = 0.33: The score is 0.33 because while sentence 2 can be attributed to the 1st node in the retrieval context regarding the use of ground coffee, sentences 1 and 3 lack any corresponding information in the retrieval context.
- deepeval / ruim / q7 / Fidelidade = 0.00: The score is 0.00 because the actual output incorrectly claims that the information was not found, whereas the retrieval context actually provides detailed information about the Aurora K2 coffee maker.
- deepeval / ruim / q7 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and comprehensively addresses both parts of the input by explaining the meaning of error code E2 and providing clear steps to resolve it without any irrelevant information.
- deepeval / ruim / q7 / Precisão do contexto = 0.00: The score is 0.00 because all retrieval nodes are irrelevant to the input. Specifically, the first node in the retrieval contexts is irrelevant because it states that "O documento fala sobre 'Especificações técnicas. A Aurora K2 é uma cafeteira...', o que não menciona o código de erro E2.", and the second node is also irrelevant because it mentions that "O documento aborda o 'Preparo do café', mas
- deepeval / ruim / q7 / Cobertura do contexto = 0.00: The score is 0.00 because all sentences in the expected output lack corresponding support in the node(s) in retrieval context; sentence 1's mention of insufficient pressure is absent, sentence 2's cause of coarse grinding is not supported by node 2, and sentence 3's specific analogy for fine grinding goes beyond the information provided in node 2.
- deepeval / ruim / q8 / Fidelidade = 0.00: The score is 0.00 because the actual output incorrectly claims that no information was found, whereas the context actually contains various details about the K2 and Aurora K1 coffee makers.
- deepeval / ruim / q8 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses the input without containing any irrelevant statements.
- deepeval / ruim / q8 / Precisão do contexto = 0.00: The score is 0.00 because all retrieved nodes are irrelevant. Specifically, the first node incorrectly discusses the capacity of 'Aurora K1' and 'Aurora K2' instead of 'Aurora K3', and the second node only lists technical specifications for 'Aurora K2' ('Reservatório de água removível de 1,4 litro') without containing information about the 'Aurora K3'. Therefore, no relevant nodes were retrieved t
- deepeval / ruim / q8 / Cobertura do contexto = 0.00: The score is 0.00 because the entire expected output regarding the Aurora K3 model and its 2027 announcement cannot be attributed to the 1st and 2nd nodes in the retrieval context, which only contain information about the Aurora K1 and Aurora K2 models.
- deepeval / bom / q1 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / bom / q1 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses all parts of the input regarding the Aurora K2's pump pressure and weight without including any irrelevant information. Great job!
- deepeval / bom / q1 / Precisão do contexto = 1.00: The score is 1.00 because all retrieval context nodes are relevant and perfectly ranked! The first node establishes that the Aurora K2 has a 'bomba de 15 bar', the second node reinforces this with 'K2 tem bomba de 15 bar', and the third node completes the picture by providing both the pump pressure and the 'Peso de 4,2 kg', ensuring a flawless retrieval process!
- deepeval / bom / q1 / Cobertura do contexto = 1.00: The score is 1.00 because all information regarding the 15 bar pump and the 4.2 kg weight in the expected output is fully supported by the node(s) in retrieval context (specifically nodes 1 and 3). Excellent retrieval accuracy!
- deepeval / bom / q2 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions detected. Great job!
- deepeval / bom / q2 / Relevância da resposta = 0.67: The score is 0.67 because while it correctly addresses part of the question regarding the espresso machine, it includes an irrelevant tip about filtered water instead of directly specifying the exact descaling interval for hard water.
- deepeval / bom / q2 / Precisão do contexto = 1.00: The score is 1.00 because all relevant nodes are perfectly ranked at the top! Node 1 and Node 2 correctly provide the descaling frequency for hard water ("It directly answers the question by stating, 'Recomendamos usar água filtrada e descalcificar a cada 150 extrações em vez de 300' when dealing with hard water" and "It mentions the general rule of descaling 'a cada 300 extrações', which provides
- deepeval / bom / q2 / Cobertura do contexto = 1.00: The score is 1.00 because all information in the expected output is fully supported by the 1st node in the retrieval context. Fantastic job!
- deepeval / bom / q3 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / bom / q3 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses the user's question about the warranty period without including any irrelevant information. Great job!
- deepeval / bom / q3 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts is ranked highest and directly answers the question by stating that 'A Aurora K2 tem garantia legal e contratual de 12 meses'. The irrelevant nodes, which discuss third-party adapter warranty cancellations (second node) and app compatibility (third node), are correctly ranked lower, resulting in a perfect retrieval precision!
- deepeval / bom / q3 / Cobertura do contexto = 0.50: The score is 0.50 because sentence 1 in the expected output is supported by node 1 in the retrieval context, but the remaining information about registering within 30 days for an extra warranty is missing from the retrieval context.
- deepeval / bom / q4 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / bom / q4 / Relevância da resposta = 1.00: The score is 1.00 because the response completely and accurately addresses both parts of the input question without any irrelevant statements.
- deepeval / bom / q4 / Precisão do contexto = 0.33: The score is 0.33 because the only relevant node is ranked third, as the first node was 'fornece informações gerais sobre a empresa, mas não menciona quem a fundou ou quem a preside hoje' and the second node was 'totalmente irrelevante para a pergunta sobre fundadores e presidência', whereas the third node correctly states that 'A empresa foi fundada por Helena Brandt e Rogério Tancredi. Helena Br
- deepeval / bom / q4 / Cobertura do contexto = 1.00: The score is 1.00 because all information in the expected output is fully captured, with sentences correctly attributed to the 3rd node in the retrieval context.
- deepeval / bom / q5 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / bom / q5 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses all parts of the input question without including any irrelevant information.
- deepeval / bom / q5 / Precisão do contexto = 1.00: The score is 1.00 because the first retrieval context node perfectly answers the input by stating it directly provides the reason for the recall ('falha no anel de vedação da caldeira, que podia vazar vapor') and the number of affected units ('18.000 unidades'). Furthermore, the second and third retrieval context nodes are correctly ranked lower as they only mention general launch details, specifi
- deepeval / bom / q5 / Cobertura do contexto = 1.00: The score is 1.00 because all information in the expected output is fully supported by the 1st node in the retrieval context. Fantastic work!
- deepeval / bom / q6 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / bom / q6 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and accurately addresses both parts of the user's input regarding using vinegar for descaling and the machine's capsule compatibility, with no irrelevant statements.
- deepeval / bom / q6 / Precisão do contexto = 0.83: The score is 0.83 because while the first and third retrieval context nodes are relevant—providing the answers that 'Nunca use vinagre: ele danifica a vedação de silicone da caldeira' and 'A Aurora K2 funciona apenas com café moído. Não existe adaptador oficial para cápsulas'—the second retrieval context node is irrelevant as 'It discusses the red blinking light for descaling, which is not directl
- deepeval / bom / q6 / Cobertura do contexto = 1.00: The score is 1.00 because all sentences in the expected output are fully supported by the node(s) in retrieval context, with the first node confirming the warning about vinegar and the third node confirming the details about ground coffee and capsules.
- deepeval / bom / q7 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with zero contradictions!
- deepeval / bom / q7 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and comprehensively answers what the error code E2 means and how to resolve it, with no irrelevant information included.
- deepeval / bom / q7 / Precisão do contexto = 1.00: The score is 1.00 because all the relevant nodes are perfectly positioned at the top! Specifically, the first node in the retrieval contexts is ranked highest because it directly defines the error code 'E2: pressão insuficiente, verifique a moagem', which is the core of the expected output, followed closely by the second node which explains the cause and solution for the error by stating 'Moagem g
- deepeval / bom / q7 / Cobertura do contexto = 1.00: The score is 1.00 because all sentences in the expected output are successfully attributed to the nodes in the retrieval context, with sentence 1 matched by the 1st node, and sentences 2 and 3 fully supported by the 2nd node!
- deepeval / bom / q8 / Fidelidade = 0.00: The score is 0.00 because the actual output incorrectly states that the information was not found, whereas the retrieval context actually provides diverse information about the Aurora K2.
- deepeval / bom / q8 / Relevância da resposta = 1.00: The score is 1.00 because the response directly and accurately addresses the input without containing any irrelevant statements. Excellent job!
- deepeval / bom / q8 / Precisão do contexto = 0.00: The score is 0.00 because all retrieval context nodes are irrelevant and failed to provide information about the Aurora K3 water reservoir capacity. Specifically, the first node (rank 1) was deemed irrelevant because "O contexto menciona a 'Aurora K2', mas a pergunta e a resposta tratam da 'Aurora K3', portanto não é útil.", the second node (rank 2) was irrelevant because "O texto fala sobre as di
- deepeval / bom / q8 / Cobertura do contexto = 0.00: The score is 0.00 because sentences 1 and 2 of the expected output cannot be attributed to any node(s) in retrieval context, as the context only discusses the Aurora K1 and K2 models and contains no information regarding the Aurora K3.
- deepeval / bm25 / q1 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / bm25 / q1 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses all parts of the input regarding the Aurora K2's pump pressure and weight without including any irrelevant information.
- deepeval / bm25 / q1 / Precisão do contexto = 0.50: The score is 0.50 because while the second node in the retrieval contexts is relevant, stating 'O texto é útil porque menciona que a Aurora K2 possui uma 'bomba de 15 bar'.', it is not ranked first. Instead, the first node in the retrieval contexts, which is irrelevant because 'O texto menciona códigos de erro, mas não fornece informações sobre a pressão da bomba ou o peso da Aurora K2.', is incor
- deepeval / bm25 / q1 / Cobertura do contexto = 0.00: The score is 0.00 because the machine weight mentioned in the expected output is absent from the nodes in the retrieval context.
- deepeval / bm25 / q2 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / bm25 / q2 / Relevância da resposta = 0.50: The score is 0.50 because, while it partially addresses the question about descaling frequency, it includes a repetitive statement that fails to provide actionable advice.
- deepeval / bm25 / q2 / Precisão do contexto = 1.00: The score is 1.00 because all the relevant retrieval context nodes are perfectly ranked at the top, allowing the model to seamlessly access the exact descaling frequency for hard water in the first node ('Recomendamos usar água filtrada e descalcificar a cada 150 extrações em vez de 300') and the standard baseline in the second node, while successfully placing the irrelevant third node—which only 
- deepeval / bm25 / q2 / Cobertura do contexto = 1.00: The score is 1.00 because all information in the expected output is fully supported by the 1st node in the retrieval context. Great job!
- deepeval / bm25 / q3 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / bm25 / q3 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses the user's question about the warranty period for the Aurora K2 without including any irrelevant information.
- deepeval / bm25 / q3 / Precisão do contexto = 0.50: The score is 0.50 because the relevant node in the retrieval contexts (the second node) is not ranked at the top. It should be ranked higher than the irrelevant nodes, such as the first node because 'The text discusses capsule usage and adapters, which is irrelevant to the warranty duration of the Aurora K2', and the third node because 'The text is about the 'Modo de economia de energia', which ha
- deepeval / bm25 / q3 / Cobertura do contexto = 0.50: The score is 0.50 because sentence 1 in the expected output is supported by the 2nd node in the retrieval context, while sentence 2 regarding the extra 12 months of warranty cannot be found in any node in the retrieval context.
- deepeval / bm25 / q4 / Fidelidade = 0.00: The score is 0.00 because the actual output incorrectly claims that the information regarding Caffeo could not be found, whereas the retrieval context actually contains diverse details about it.
- deepeval / bm25 / q4 / Relevância da resposta = 1.00: The score is 1.00 because the actual output directly and accurately answers both parts of the input without including any irrelevant information.
- deepeval / bm25 / q4 / Precisão do contexto = 0.00: The score is 0.00 because all retrieval context nodes are irrelevant. Specifically, the first node discusses how to extend the warranty, which "não tem relação com quem fundou ou preside a Caffeo Brasil". The second node talks about technical assistance, and the third node mentions that "A Caffeo Brasil é uma fabricante de eletrodomésticos para café fundada em 2014", but "não cita os nomes de Hele
- deepeval / bm25 / q4 / Cobertura do contexto = 0.00: The score is 0.00 because sentences 1 and 2 of the expected output regarding the founders and the president cannot be attributed to any information in the 3rd node in the retrieval context.
- deepeval / bm25 / q5 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with zero contradictions!
- deepeval / bm25 / q5 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses all parts of the user's input regarding the Aurora K1 recall without including any irrelevant information. Great job!
- deepeval / bm25 / q5 / Precisão do contexto = 1.00: The score is 1.00 because the first retrieval context node perfectly answers why the Aurora K1 was recalled ("falha no anel de vedação da caldeira, que podia vazar vapor") and how many units were affected ("18.000 unidades"), and it is correctly ranked above the irrelevant nodes. The second retrieval context node ("It discusses the successor Aurora K2, which is not relevant to the recall of the Au
- deepeval / bm25 / q5 / Cobertura do contexto = 1.00: The score is 1.00 because all information in the expected output is fully supported by node(s) in retrieval context! Fantastic job retrieving all the exact details!
- deepeval / bm25 / q6 / Fidelidade = 0.67: The score is 0.67 because the actual output incorrectly states that the information was not found in the available sources, whereas the context actually contains specific facts about the Aurora K2.
- deepeval / bm25 / q6 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and accurately addresses both parts of the user's input regarding descaling with vinegar and capsule compatibility without any irrelevant information.
- deepeval / bm25 / q6 / Precisão do contexto = 1.00: The score is 1.00 because all relevant nodes containing information about capsules and descalcification are perfectly ranked above the irrelevant node discussing the milk frother.
- deepeval / bm25 / q6 / Cobertura do contexto = 0.50: The score is 0.50 because sentence 1 regarding vinegar damaging the silicone seal cannot be attributed to any node(s) in retrieval context, while sentence 2 is successfully supported by the 1st node in the retrieval context.
- deepeval / bm25 / q7 / Fidelidade = 0.50: The score is 0.50 because the actual output incorrectly recommends using a fine grind like refined sugar to fix error code E2, whereas the context states that error E2 is actually caused by the grind being too coarse, and that too fine of a grind can clog the filter.
- deepeval / bm25 / q7 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and comprehensively addresses the input regarding the meaning and solution for error code E2, with no irrelevant statements included. Great job!
- deepeval / bm25 / q7 / Precisão do contexto = 1.00: The score is 1.00 because all relevant nodes are perfectly positioned above any irrelevant ones! The first node correctly explains that 'Moagem grossa demais causa café aguado e o código de erro E2' and the second node directly defines that 'E2: pressão insuficiente, verifique a moagem', and both are ranked higher than the third node, which only discusses 'luz vermelha piscando e descalcificação, 
- deepeval / bm25 / q7 / Cobertura do contexto = 1.00: The score is 1.00 because all sentences in the expected output—specifically sentence 1 regarding E2 being insufficient pressure (supported by node 2 in the retrieval context), sentence 2 regarding the common cause of a too coarse grind (supported by node 1), and sentence 3 regarding the solution to use a fine grind (supported by node 1)—are fully accounted for with flying colors!
- deepeval / bm25 / q8 / Fidelidade = 0.00: The score is 0.00 because the actual output incorrectly claims that the information was not found, whereas the retrieval context actually contains several detailed pieces of information about the Aurora K2 and Aurora K3 coffee makers and their cleaning instructions.
- deepeval / bm25 / q8 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses the input without containing any irrelevant statements.
- deepeval / bm25 / q8 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts is ranked at the top and directly supports the expected output by stating that 'A Caffeo anunciou em 2025 que desenvolve a Aurora K3... Nenhuma especificação foi divulgada'. This ensures that the only relevant information is prioritized above the irrelevant nodes, which are correctly ranked lower: the second node in the retrieval c
- deepeval / bm25 / q8 / Cobertura do contexto = 1.00: The score is 1.00 because all sentences in the expected output are fully supported by the information found in the 1st node in the retrieval context! Excellent retrieval!
- deepeval / arvore / q1 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / arvore / q1 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses all parts of the input regarding the Aurora K2's pump pressure and weight without including any irrelevant information. Great job!
- deepeval / arvore / q1 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts successfully provides the exact information needed regarding the pump pressure and weight of the Aurora K2, stating that 'O documento fornece todas as informações necessárias sobre a Aurora K2, especificando que ela possui uma 'bomba de 15 bar' e um 'Peso de 4,2 kg', o que corresponde exatamente ao resultado esperado.'!
- deepeval / arvore / q1 / Cobertura do contexto = 1.00: The score is 1.00 because all information in the expected output is fully supported by node(s) in the retrieval context, specifically confirming the 15 bar pump and 4.2 kg weight of the Aurora K2!
- deepeval / arvore / q2 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / arvore / q2 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses the question about descaling the Aurora K2 with hard water, with zero irrelevant statements.
- deepeval / arvore / q2 / Precisão do contexto = 0.50: The score is 0.50 because the irrelevant first node, which states 'O contexto menciona a base geral de 'Descalcifique a cada 300 extrações', mas não é o mais específico para a condição de água dura.', is ranked higher than the relevant second node, which states 'O texto afirma diretamente que 'Água dura acelera o acúmulo de calcário. Recomendamos usar água filtrada e descalcificar a cada 150 extra
- deepeval / arvore / q2 / Cobertura do contexto = 1.00: The score is 1.00 because all information in sentence 1 of the expected output is fully supported by the 2nd node in the retrieval context, ensuring perfect recall!
- deepeval / arvore / q3 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions detected. Great job!
- deepeval / arvore / q3 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses the user's question about the warranty period without any irrelevant information.
- deepeval / arvore / q3 / Precisão do contexto = 1.00: The score is 1.00 because all relevant nodes are perfectly ranked at the top! The first node explicitly states that 'A Aurora K2 tem garantia legal e contratual de 12 meses contra defeitos de fabricação', and the second node usefully details that 'Quem cadastra a máquina no site da Caffeo em até 30 dias após a compra ganha 12 meses adicionais, totalizando 24 meses de garantia'.
- deepeval / arvore / q3 / Cobertura do contexto = 1.00: The score is 1.00 because all information in the expected output is fully supported by the 1st and 2nd nodes in the retrieval context. Fantastic job!
- deepeval / arvore / q4 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / arvore / q4 / Relevância da resposta = 1.00: The score is 1.00 because the response directly and accurately answers both parts of the user's input without including any irrelevant statements.
- deepeval / arvore / q4 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts perfectly answers the input by stating that 'A empresa foi fundada por Helena Brandt e Rogério Tancredi' and that 'Helena Brandt é a presidente desde a fundação.'!
- deepeval / arvore / q4 / Cobertura do contexto = 1.00: The score is 1.00 because all information regarding the founding of Caffeo Brasil and Helena Brandt's presidency in the expected output is fully supported by the 1st node in the retrieval context. Excellent retrieval performance!
- deepeval / arvore / q5 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / arvore / q5 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses all parts of the user's input without including any irrelevant information. Great job!
- deepeval / arvore / q5 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts successfully and directly addresses the input by explaining that 'Em agosto de 2019 a Caffeo fez um recall voluntário de 18.000 unidades da Aurora K1 por falha no anel de vedação da caldeira, que podia vazar vapor', providing both the reason for the recall and the number of affected units perfectly right at the top!
- deepeval / arvore / q5 / Cobertura do contexto = 1.00: The score is 1.00 because all sentences in the expected output are fully supported by the 1st node in the retrieval context. Fantastic job!
- deepeval / arvore / q6 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / arvore / q6 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and accurately addresses both parts of the user's input regarding using vinegar for descaling and the machine's capsule compatibility, with no irrelevant statements.
- deepeval / arvore / q6 / Precisão do contexto = 1.00: The score is 1.00 because all relevant retrieval context nodes are perfectly ranked at the top, with the first node explicitly stating 'Nunca use vinagre: ele danifica a vedação de silicone da caldeira.' and the second node confirming that 'A Aurora K2 funciona apenas com café moído. Não existe adaptador oficial para cápsulas', addressing the input wonderfully!
- deepeval / arvore / q6 / Cobertura do contexto = 1.00: The score is 1.00 because all sentences in the expected output are fully supported by the information found in node(s) in retrieval context 1 and 2, ensuring perfect recall!
- deepeval / arvore / q7 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / arvore / q7 / Relevância da resposta = 1.00: The score is 1.00 because the response perfectly and directly addresses the user's question about the meaning and solution for error code E2, with zero irrelevant statements.
- deepeval / arvore / q7 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts perfectly answers the user's question about the error code E2, stating that it means 'pressão insuficiente, verifique a moagem', and provides the necessary solution in its reason!
- deepeval / arvore / q7 / Cobertura do contexto = 0.33: The score is 0.33 because sentence 1 in the expected output is successfully attributed to node 1 in the retrieval context, but sentences 2 and 3 cannot be attributed to the 1st node in the retrieval context as they contain unmentioned details about the common cause and specific grinding solution.
- deepeval / arvore / q8 / Fidelidade = 0.00: The score is 0.00 because the actual output fails to include the specific information from the retrieval context regarding the Aurora K3, such as its development by Caffeo in 2025, its integrated grinder, and its projected launch in 2027.
- deepeval / arvore / q8 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses the input without containing any irrelevant information.
- deepeval / arvore / q8 / Precisão do contexto = 1.00: The score is 1.00 because the only retrieval context is directly relevant and ranked first, providing the necessary information!
- deepeval / arvore / q8 / Cobertura do contexto = 1.00: The score is 1.00 because all sentences in the expected output—specifically sentence 1 and sentence 2—are fully supported by the 1st node in the retrieval context. Outstanding job!
- deepeval / agentico / q1 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with zero contradictions!
- deepeval / agentico / q1 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses all parts of the input regarding the Aurora K2's pump pressure and weight without including any irrelevant information.
- deepeval / agentico / q1 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts successfully and directly provides all the necessary information, stating that 'A Aurora K2 é uma cafeteira de café moído com bomba de 15 bar' and that it has a 'Peso de 4,2 kg', perfectly answering both parts of the input right at the top!
- deepeval / agentico / q1 / Cobertura do contexto = 1.00: The score is 1.00 because all information regarding the Aurora K2 pump pressure and weight in sentence 1 of the expected output is fully supported by the 1st node in the retrieval context. Excellent!
- deepeval / agentico / q2 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / agentico / q2 / Relevância da resposta = 1.00: The score is 1.00 because the response directly and accurately addresses the user's question regarding the descaling frequency for the Aurora K2 with hard water, containing no irrelevant information.
- deepeval / agentico / q2 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts correctly answers the question, stating that 'Recomendamos usar água filtrada e descalcificar a cada 150 extrações em vez de 300' for hard water, and it is perfectly ranked above the second node, which only mentions the general standard of 'Descalcifique a cada 300 extrações'. Fantastic retrieval!
- deepeval / agentico / q2 / Cobertura do contexto = 1.00: The score is 1.00 because all information in the expected output is fully supported by node(s) in the retrieval context, ensuring perfect recall!
- deepeval / agentico / q3 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / agentico / q3 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and accurately addresses the user's question regarding the warranty period of the Aurora K2 without any irrelevant information.
- deepeval / agentico / q3 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts is directly relevant, stating that 'A Aurora K2 tem garantia legal e contratual de 12 meses contra defeitos de fabricação', successfully answering the user's question on the first try!
- deepeval / agentico / q3 / Cobertura do contexto = 0.50: The score is 0.50 because sentence 1 in the expected output is supported by information in the 1st node in the retrieval context regarding the standard warranty, but sentence 2 lacks any supporting information in the retrieval context about registering the machine for an extended warranty.
- deepeval / agentico / q4 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions detected. Great job!
- deepeval / agentico / q4 / Relevância da resposta = 1.00: The score is 1.00 because the actual output completely and accurately addresses the input without containing any irrelevant statements.
- deepeval / agentico / q4 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts is directly relevant, successfully providing both the founders and the current president as requested!
- deepeval / agentico / q4 / Cobertura do contexto = 1.00: The score is 1.00 because all sentences in the expected output are fully supported by the 1st node in the retrieval context. Fantastic job!
- deepeval / agentico / q5 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / agentico / q5 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses all parts of the input regarding the Aurora K1 recall without including any irrelevant information.
- deepeval / agentico / q5 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts is directly relevant, perfectly addressing the recall reason ('falha no anel de vedação da caldeira, que podia vazar vapor') and the affected units ('18.000 unidades') right at the top! Outstanding retrieval performance!
- deepeval / agentico / q5 / Cobertura do contexto = 1.00: The score is 1.00 because all sentences in the expected output are fully supported by node(s) in the retrieval context, ensuring a complete and accurate retrieval!
- deepeval / agentico / q6 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / agentico / q6 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and accurately addresses the user's question about using vinegar for descaling in a capsule coffee machine without including any irrelevant information.
- deepeval / agentico / q6 / Precisão do contexto = 1.00: The score is 1.00 because all relevant nodes are perfectly ranked at the top! The first retrieval context node directly states 'Nunca use vinagre: ele danifica a vedação de silicone da caldeira', and the second retrieval context node clearly answers whether the machine accepts capsules by stating 'Não. A Aurora K2 funciona apenas com café moído. Não existe adaptador oficial para cápsulas'.
- deepeval / agentico / q6 / Cobertura do contexto = 1.00: The score is 1.00 because all information in the expected output is fully supported by the nodes in the retrieval context: the first sentence is backed by the 1st node regarding the damage caused by vinegar, and the second sentence is confirmed by the 2nd node regarding the use of ground coffee.
- deepeval / agentico / q7 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / agentico / q7 / Relevância da resposta = 1.00: The score is 1.00 because the response is completely relevant to the input, directly addressing the meaning of the E2 error code and how to resolve it without any extraneous information.
- deepeval / agentico / q7 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts is directly relevant, perfectly addressing the meaning and solution for the error code E2 by explaining that it is 'pressão insuficiente' and advising to 'verifique a moagem'! Stellar retrieval!
- deepeval / agentico / q7 / Cobertura do contexto = 1.00: The score is 1.00 because all sentences in the expected output—identifying E2 as insufficient pressure (sentence 1), pointing to a too-coarse grind as the common cause (sentence 2), and suggesting a fine grind similar to refined sugar as the solution (sentence 3)—are fully supported by information found in the 1st node in the retrieval context.
- deepeval / agentico / q8 / Fidelidade = 0.00: The score is 0.00 because the actual output incorrectly states that the Aurora K3 was developed by Caffeo in 2025 with an integrated grinder and a launch scheduled for 2027, which contradicts the retrieval context.
- deepeval / agentico / q8 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses the input without containing any irrelevant information. Great job!
- deepeval / agentico / q8 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts is directly relevant, perfectly capturing the lack of information regarding the water reservoir capacity of the Aurora K3 with the reason: "O contexto menciona que a 'Aurora K3' foi anunciada para '2027' e afirma explicitamente que 'Nenhuma especificação foi divulgada', o que sustenta diretamente a resposta esperada de que não há e
- deepeval / agentico / q8 / Cobertura do contexto = 1.00: The score is 1.00 because all information regarding the Aurora K3 being announced for 2027 with no specifications is fully supported by the 1st node in the retrieval context. Perfect recall!
- deepeval / grafo / q1 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions detected. Great job!
- deepeval / grafo / q1 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses all parts of the input regarding the Aurora K2's pump pressure and weight without including any irrelevant information. Great job!
- deepeval / grafo / q1 / Precisão do contexto = 1.00: The score is 1.00 because all the relevant nodes containing the required information are perfectly ranked at the very top, ensuring optimal precision right out of the gate!
- deepeval / grafo / q1 / Cobertura do contexto = 0.00: The score is 0.00 because, while the first part about the Aurora K2 pump having 15 bar can be attributed to node(s) in retrieval context 1, the claim regarding the machine weighing 4.2 kg cannot be found in any of the retrieval contexts.
- deepeval / grafo / q2 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / grafo / q2 / Relevância da resposta = 1.00: The score is 1.00 because the response directly and accurately addresses the user's question regarding the descaling frequency for the Aurora K2 with hard water, containing no irrelevant statements.
- deepeval / grafo / q2 / Precisão do contexto = 0.83: The score is 0.83 because the first node is relevant, stating that one should 'Descalcifique a cada 300 extrações'. The third node is also relevant, mentioning 'obstrução por água com alto teor de calcário'. However, the score is not higher because the second node, which discusses the 'Recall da K1', is irrelevant to the frequency of descaling the Aurora K2 and is ranked higher than the third rele
- deepeval / grafo / q2 / Cobertura do contexto = 0.00: The score is 0.00 because the sentence in the expected output regarding the 150-extraction interval for hard water cannot be attributed to any node in the retrieval context, as the 1st node only mentions a 300-extraction interval and the 3rd node only mentions obstruction due to high limestone water without specifying the number.
- deepeval / grafo / q3 / Fidelidade = 0.00: The score is 0.00 because the actual output incorrectly claims that the information was not found, whereas the retrieval context actually contains various details about both the Aurora K1 and Aurora K3.
- deepeval / grafo / q3 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses the user's question without including any irrelevant information. Great job!
- deepeval / grafo / q3 / Precisão do contexto = 0.00: The score is 0.00 because all retrieved nodes are irrelevant to the input about the warranty time of the Aurora K2. Specifically, the first node discusses the 'Recall da K1' ("O texto fala sobre o 'Recall da K1' e não menciona informações sobre o tempo de garantia da Aurora K2."), the second node covers 'Descalcificação' ("O texto trata sobre 'Descalcificação' e cuidados com a máquina, sem conter 
- deepeval / grafo / q3 / Cobertura do contexto = 0.00: The score is 0.00 because the information regarding the 12-month standard warranty and the 24-month extended warranty upon registration in the expected output cannot be found in any of the nodes in retrieval context, which only cover product recalls and descalcification instructions.
- deepeval / grafo / q4 / Fidelidade = 0.00: The score is 0.00 because the actual output incorrectly claims that the information was not found, whereas the context actually provides details regarding the warranty, production, employees, components, price, and sales locations of the Aurora K2.
- deepeval / grafo / q4 / Relevância da resposta = 1.00: The score is 1.00 because the response directly and accurately addresses both parts of the input question without any irrelevant statements.
- deepeval / grafo / q4 / Precisão do contexto = 0.00: The score is 0.00 because all retrieval context nodes are irrelevant to the input. Specifically, the first node discusses how to extend the warranty for Caffeo machines, the second node discusses the factory in Caxias do Sul and component sourcing, and the third node discusses the price and sales channels of the Aurora K2, none of which provide information on who founded Caffeo Brasil or who presi
- deepeval / grafo / q4 / Cobertura do contexto = 0.00: The score is 0.00 because the 1st sentence regarding the founders and the 2nd sentence regarding the company president cannot be attributed to any information across all nodes in the retrieval context.
- deepeval / grafo / q5 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely accurate and perfectly aligned with the retrieval context. Great job!
- deepeval / grafo / q5 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and accurately answers both parts of the input regarding the reason for the Aurora K1 recall and the number of affected units without any irrelevant information. Great job!
- deepeval / grafo / q5 / Precisão do contexto = 0.50: The score is 0.50 because the second retrieval node, which directly answers the question about the Aurora K1 recall and affected units, is ranked second instead of first. It should be ranked higher than the first retrieval node, which only talks about 'Aurora K2 and its differences from the K1, which is not about the recall of the K1,' and the third retrieval node, which 'discusses descaling instr
- deepeval / grafo / q5 / Cobertura do contexto = 1.00: The score is 1.00 because all information regarding the August 2019 recall (sentences 1 and 2) is fully supported by node 2 in the retrieval context. Excellent job!
- deepeval / grafo / q6 / Fidelidade = 1.00: The score is 1.00 because the actual output is completely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / grafo / q6 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and accurately answers both parts of the user's question regarding descaling with vinegar and capsule compatibility without any irrelevant information.
- deepeval / grafo / q6 / Precisão do contexto = 1.00: The score is 1.00 because the first node in the retrieval contexts is the only relevant one, correctly explaining that 'Nunca use vinagre: ele danifica a vedação de silicone da caldeira.' It successfully outranks the second node, which discusses daily cleaning that 'is not relevant to whether the machine accepts capsules or if vinegar can be used for descaling,' and the third node, which merely me
- deepeval / grafo / q6 / Cobertura do contexto = 0.33: The score is 0.33 because sentence 1 is successfully attributed to node 1 in the retrieval context, which explains that vinegar damages the silicone seal, but sentences 2 and 3 lack matching information in the context.
- deepeval / grafo / q7 / Fidelidade = 1.00: The score is 1.00 because the actual output is entirely faithful to the retrieval context with no contradictions found. Great job!
- deepeval / grafo / q7 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and comprehensively answers what the error code E2 means and how to resolve it, with no irrelevant statements.
- deepeval / grafo / q7 / Precisão do contexto = 1.00: The score is 1.00 because all retrieval contexts are perfectly relevant and ranked in the ideal order! The first node correctly explains that 'O texto explica diretamente o significado do código de erro ao afirmar que 'E2: pressão insuficiente, verifique a moagem.'', and the second node provides the exact solution by stating that 'Moagem grossa demais causa café aguado e o código de erro E2' and t
- deepeval / grafo / q7 / Cobertura do contexto = 1.00: The score is 1.00 because all sentences in the expected output are fully supported by the nodes in retrieval context, with sentence 1 matched to the 1st node, and sentences 2 and 3 successfully matched to the 2nd node! Fantastic job!
- deepeval / grafo / q8 / Fidelidade = 0.00: The score is 0.00 because the actual output incorrectly claims that no information was found, whereas the context actually contains various details about the K1 and K2 coffee makers.
- deepeval / grafo / q8 / Relevância da resposta = 1.00: The score is 1.00 because the output directly and completely addresses the input without containing any irrelevant statements. Excellent job!
- deepeval / grafo / q8 / Precisão do contexto = 0.00: The score is 0.00 because all nodes in the retrieval contexts are irrelevant. Specifically, the first node states that "não há essa informação" regarding the water reservoir capacity of the Aurora K3, the second node discusses "Recall da K1" which is irrelevant, and the third node addresses hard water and limescale without containing information about the Aurora K3.
- deepeval / grafo / q8 / Cobertura do contexto = 0.50: The score is 0.50 because sentence 1 correctly indicates that the information is missing based on node(s) in retrieval context, while sentence 2 incorrectly claims the Aurora K3 was announced for 2027, which is not supported by any of the nodes.
- promptfoo / ruim / q1 / Fidelidade = 1.00: Faithfulness 1.00 is >= 0.5
- promptfoo / ruim / q1 / Relevância da resposta = 0.96: Relevance 0.96 is greater than threshold 0.5
- promptfoo / ruim / q1 / Precisão do contexto = 0.67: Context relevance 0.67 is >= 0.5
- promptfoo / ruim / q1 / Cobertura do contexto = 0.50: Recall 0.50 is >= 0.5
- promptfoo / ruim / q2 / Fidelidade = 1.00: Faithfulness 1.00 is >= 0.5
- promptfoo / ruim / q2 / Relevância da resposta = 0.80: Relevance 0.80 is greater than threshold 0.5
- promptfoo / ruim / q2 / Precisão do contexto = 0.00: Grader output does not quote the provided context
- promptfoo / ruim / q2 / Cobertura do contexto = –: ERRO do juiz: Grader returned no [Attributed]/[Not Attributed] classifications
- promptfoo / ruim / q3 / Fidelidade = 1.00: Faithfulness 1.00 is >= 0.5
- promptfoo / ruim / q3 / Relevância da resposta = 0.48: Relevance 0.48 is less than threshold 0.5
- promptfoo / ruim / q3 / Precisão do contexto = 0.00: Context relevance 0.00 is < 0.5
- promptfoo / ruim / q3 / Cobertura do contexto = 0.00: Recall 0.00 is < 0.5
- promptfoo / ruim / q4 / Fidelidade = 0.67: Faithfulness 0.67 is >= 0.5
- promptfoo / ruim / q4 / Relevância da resposta = 0.68: Relevance 0.68 is greater than threshold 0.5
- promptfoo / ruim / q4 / Precisão do contexto = 0.33: Context relevance 0.33 is < 0.5
- promptfoo / ruim / q4 / Cobertura do contexto = –: ERRO do juiz: Grader returned no [Attributed]/[Not Attributed] classifications
- promptfoo / ruim / q5 / Fidelidade = 1.00: Faithfulness 1.00 is >= 0.5
- promptfoo / ruim / q5 / Relevância da resposta = 0.86: Relevance 0.86 is greater than threshold 0.5
- promptfoo / ruim / q5 / Precisão do contexto = 0.33: Context relevance 0.33 is < 0.5
- promptfoo / ruim / q5 / Cobertura do contexto = 1.00: Recall 1.00 is >= 0.5
- promptfoo / ruim / q6 / Fidelidade = 0.00: Faithfulness 0.00 is < 0.5
- promptfoo / ruim / q6 / Relevância da resposta = 0.47: Relevance 0.47 is less than threshold 0.5
- promptfoo / ruim / q6 / Precisão do contexto = 0.00: Context relevance 0.00 is < 0.5
- promptfoo / ruim / q6 / Cobertura do contexto = 0.33: Recall 0.33 is < 0.5
- promptfoo / ruim / q7 / Fidelidade = 1.00: Faithfulness 1.00 is >= 0.5
- promptfoo / ruim / q7 / Relevância da resposta = 0.47: Relevance 0.46 is less than threshold 0.5
- promptfoo / ruim / q7 / Precisão do contexto = 0.00: Context relevance 0.00 is < 0.5
- promptfoo / ruim / q7 / Cobertura do contexto = –: ERRO do juiz: Grader returned no [Attributed]/[Not Attributed] classifications
- promptfoo / ruim / q8 / Fidelidade = 1.00: Faithfulness 1.00 is >= 0.5
- promptfoo / ruim / q8 / Relevância da resposta = 0.48: Relevance 0.48 is less than threshold 0.5
- promptfoo / ruim / q8 / Precisão do contexto = 0.00: Context relevance 0.00 is < 0.5
- promptfoo / ruim / q8 / Cobertura do contexto = 0.00: Recall 0.00 is < 0.5
- promptfoo / bom / q1 / Fidelidade = 1.00: Faithfulness 1.00 is >= 0.5
- promptfoo / bom / q1 / Relevância da resposta = 0.95: Relevance 0.95 is greater than threshold 0.5
- promptfoo / bom / q1 / Precisão do contexto = 0.60: Context relevance 0.60 is >= 0.5
- promptfoo / bom / q1 / Cobertura do contexto = 1.00: Recall 1.00 is >= 0.5
- promptfoo / bom / q2 / Fidelidade = 1.00: Faithfulness 1.00 is >= 0.5
- promptfoo / bom / q2 / Relevância da resposta = 0.74: Relevance 0.74 is greater than threshold 0.5
- promptfoo / bom / q2 / Precisão do contexto = 0.20: Context relevance 0.20 is < 0.5
- promptfoo / bom / q2 / Cobertura do contexto = –: ERRO do juiz: Grader returned no [Attributed]/[Not Attributed] classifications
- promptfoo / bom / q3 / Fidelidade = 1.00: Faithfulness 1.00 is >= 0.5
- promptfoo / bom / q3 / Relevância da resposta = 0.97: Relevance 0.97 is greater than threshold 0.5
- promptfoo / bom / q3 / Precisão do contexto = 0.00: Grader output does not quote the provided context
- promptfoo / bom / q3 / Cobertura do contexto = 0.50: Recall 0.50 is >= 0.5
- promptfoo / bom / q4 / Fidelidade = 1.00: Faithfulness 1.00 is >= 0.5
- promptfoo / bom / q4 / Relevância da resposta = 0.98: Relevance 0.98 is greater than threshold 0.5
- promptfoo / bom / q4 / Precisão do contexto = 0.20: Context relevance 0.20 is < 0.5
- promptfoo / bom / q4 / Cobertura do contexto = 1.00: Recall 1.00 is >= 0.5
- promptfoo / bom / q5 / Fidelidade = 1.00: Faithfulness 1.00 is >= 0.5
- promptfoo / bom / q5 / Relevância da resposta = 0.85: Relevance 0.85 is greater than threshold 0.5
- promptfoo / bom / q5 / Precisão do contexto = 0.20: Context relevance 0.20 is < 0.5
- promptfoo / bom / q5 / Cobertura do contexto = –: ERRO do juiz: Grader returned no [Attributed]/[Not Attributed] classifications
- promptfoo / bom / q6 / Fidelidade = 1.00: Faithfulness 1.00 is >= 0.5
- promptfoo / bom / q6 / Relevância da resposta = 0.86: Relevance 0.86 is greater than threshold 0.5
- promptfoo / bom / q6 / Precisão do contexto = 0.40: Context relevance 0.40 is < 0.5
- promptfoo / bom / q6 / Cobertura do contexto = 0.67: Recall 0.67 is >= 0.5
- promptfoo / bom / q7 / Fidelidade = 1.00: Faithfulness 1.00 is >= 0.5
- promptfoo / bom / q7 / Relevância da resposta = 1.00: Relevance 1.00 is greater than threshold 0.5
- promptfoo / bom / q7 / Precisão do contexto = 0.40: Context relevance 0.40 is < 0.5
- promptfoo / bom / q7 / Cobertura do contexto = 1.00: Recall 1.00 is >= 0.5
- promptfoo / bom / q8 / Fidelidade = 1.00: Faithfulness 1.00 is >= 0.5
- promptfoo / bom / q8 / Relevância da resposta = 0.48: Relevance 0.48 is less than threshold 0.5
- promptfoo / bom / q8 / Precisão do contexto = 0.00: Context relevance 0.00 is < 0.5
- promptfoo / bom / q8 / Cobertura do contexto = 0.50: Recall 0.50 is >= 0.5
