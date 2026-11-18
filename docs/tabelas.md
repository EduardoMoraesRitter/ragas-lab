# Tabelas geradas (src/relatorio.py)

## 1. Média por ferramenta e por RAG

| Ferramenta | RAG | Fidelidade | Relevância da resposta | Precisão do contexto | Cobertura do contexto |
|---|---|---|---|---|---|
| ragas | vetor (bom) | 0.98 | 0.80 | 0.50 | 0.88 |
| ragas | palavras (ruim) | 0.72 | 0.42 | 0.31 | 0.58 |
| deepeval | vetor (bom) | 0.88 | 0.96 | 0.77 | 0.81 |
| deepeval | palavras (ruim) | 0.50 | 0.96 | 0.50 | 0.42 |
| promptfoo | vetor (bom) | 1.00 | 0.85 | 0.25 | 0.78 |
| promptfoo | palavras (ruim) | 0.83 | 0.65 | 0.17 | 0.37 |

## 2. Fidelidade por pergunta (bom / ruim)

| Pergunta | ragas | deepeval | promptfoo |
|---|---|---|---|
| q1 | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / 1.00 |
| q2 | 1.00 / 0.75 | 1.00 / 1.00 | 1.00 / 1.00 |
| q3 | 1.00 / 1.00 | 1.00 / 0.00 | 1.00 / 1.00 |
| q4 | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / 0.67 |
| q5 | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / 1.00 |
| q6 | 1.00 / 0.00 | 1.00 / 0.00 | 1.00 / 0.00 |
| q7 | 0.83 / 0.00 | 1.00 / 0.00 | 1.00 / 1.00 |
| q8 | 1.00 / 1.00 | 0.00 / 0.00 | 1.00 / 1.00 |

## 2. Relevância da resposta por pergunta (bom / ruim)

| Pergunta | ragas | deepeval | promptfoo |
|---|---|---|---|
| q1 | 0.95 / 0.99 | 1.00 / 1.00 | 0.95 / 0.96 |
| q2 | 0.77 / 0.81 | 0.67 / 0.67 | 0.74 / 0.80 |
| q3 | 0.97 / 0.00 | 1.00 / 1.00 | 0.97 / 0.48 |
| q4 | 0.98 / 0.70 | 1.00 / 1.00 | 0.98 / 0.68 |
| q5 | 0.87 / 0.88 | 1.00 / 1.00 | 0.85 / 0.86 |
| q6 | 0.88 / 0.00 | 1.00 / 1.00 | 0.86 / 0.47 |
| q7 | 1.00 / 0.00 | 1.00 / 1.00 | 1.00 / 0.47 |
| q8 | 0.00 / 0.00 | 1.00 / 1.00 | 0.48 / 0.48 |

## 2. Precisão do contexto por pergunta (bom / ruim)

| Pergunta | ragas | deepeval | promptfoo |
|---|---|---|---|
| q1 | 0.33 / 0.00 | 1.00 / 1.00 | 0.60 / 0.67 |
| q2 | 1.00 / 1.00 | 1.00 / 1.00 | 0.20 / 0.00 |
| q3 | 0.00 / 0.00 | 1.00 / 0.00 | 0.00 / 0.00 |
| q4 | 0.33 / 0.50 | 0.33 / 0.50 | 0.20 / 0.33 |
| q5 | 1.00 / 1.00 | 1.00 / – | 0.20 / 0.33 |
| q6 | 0.33 / 0.00 | 0.83 / 1.00 | 0.40 / 0.00 |
| q7 | 1.00 / 0.00 | 1.00 / 0.00 | 0.40 / 0.00 |
| q8 | 0.00 / 0.00 | 0.00 / 0.00 | 0.00 / 0.00 |

## 2. Cobertura do contexto por pergunta (bom / ruim)

| Pergunta | ragas | deepeval | promptfoo |
|---|---|---|---|
| q1 | 1.00 / 0.50 | 1.00 / 0.00 | 1.00 / 0.50 |
| q2 | 1.00 / 1.00 | 1.00 / 1.00 | – / – |
| q3 | 0.50 / 0.00 | 0.50 / 0.00 | 0.50 / 0.00 |
| q4 | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / – |
| q5 | 1.00 / 1.00 | 1.00 / 1.00 | – / 1.00 |
| q6 | 1.00 / 0.67 | 1.00 / 0.33 | 0.67 / 0.33 |
| q7 | 1.00 / 0.00 | 1.00 / 0.00 | 1.00 / – |
| q8 | 0.50 / 0.50 | 0.00 / 0.00 | 0.50 / 0.00 |

## 3. O que cada RAG respondeu

### q1. Qual é a pressão da bomba da Aurora K2 e quanto ela pesa?

Gabarito: A bomba da Aurora K2 é de 15 bar e a máquina pesa 4,2 kg.

- **bom** (trechos wiki-05, faq-10, manual-01): A cafeteira Aurora K2 possui uma bomba de 15 bar. O peso do aparelho é de 4,2 kg.
- **ruim** (trechos wiki-05, faq-10): A pressão da bomba da Aurora K2 é de 15 bar. Não encontrei essa informação nas fontes disponíveis sobre o peso dela.

### q2. A cada quantas extrações devo descalcificar a Aurora K2 se a água da minha cidade for dura?

Gabarito: Com água dura, a recomendação é descalcificar a cada 150 extrações, em vez das 300 do manual.

- **bom** (trechos faq-07, manual-04, wiki-05): Água dura acelera o acúmulo de calcário e recomendamos usar água filtrada e descalcificar a cada 150 extrações em vez de 300.
- **ruim** (trechos faq-07, manual-04): Se a água da sua cidade for dura, recomendamos descalcificar a cada 150 extrações em vez de 300. Água dura acelera o acúmulo de calcário, e danos por calcário não são cobertos pela garantia.

### q3. Quanto tempo de garantia eu tenho na Aurora K2?

Gabarito: A garantia padrão é de 12 meses. Quem cadastra a máquina no site em até 30 dias ganha mais 12 meses, totalizando 24 meses.

- **bom** (trechos manual-06, faq-02, faq-05): A Aurora K2 tem garantia legal e contratual de 12 meses contra defeitos de fabricação, contados a partir da data da nota fiscal.
- **ruim** (trechos manual-01, wiki-05): Não encontrei essa informação nas fontes disponíveis.

### q4. Quem fundou a Caffeo Brasil e quem a preside hoje?

Gabarito: A Caffeo Brasil foi fundada por Helena Brandt e Rogério Tancredi. Helena Brandt é a presidente desde a fundação.

- **bom** (trechos wiki-01, faq-08, wiki-02): A Caffeo Brasil foi fundada por Helena Brandt e Rogério Tancredi. Helena Brandt é a presidente desde a fundação.
- **ruim** (trechos faq-04, wiki-02): A empresa foi fundada por Helena Brandt e Rogério Tancredi. Helena Brandt é a presidente desde a fundação.

### q5. Por que a Aurora K1 passou por recall e quantas unidades foram afetadas?

Gabarito: O recall de agosto de 2019 foi por falha no anel de vedação da caldeira, que podia vazar vapor. Foram 18.000 unidades.

- **bom** (trechos wiki-04, wiki-03, faq-10): Em agosto de 2019, a Caffeo fez um recall voluntário da Aurora K1 devido a uma falha no anel de vedação da caldeira, que podia vazar vapor. O total de unidades afetadas foi de 18.000. Nenhum ferimento foi registrado em decorrência do problema.
- **ruim** (trechos wiki-04, wiki-05): Em agosto de 2019, a Caffeo fez um recall voluntário da Aurora K1 devido a uma falha no anel de vedação da caldeira, que podia vazar vapor. No total, 18.000 unidades foram afetadas por esse problema.

### q6. Posso usar vinagre para descalcificar e a máquina aceita cápsulas?

Gabarito: Não aos dois. Vinagre danifica a vedação de silicone da caldeira. A máquina só funciona com café moído e não existe adaptador oficial para cápsulas.

- **bom** (trechos manual-04, faq-01, faq-02): Não, você nunca deve usar vinagre para descalcificar, pois ele danifica a vedação de silicone da caldeira. Além disso, a Aurora K2 funciona apenas com café moído e não aceita cápsulas.
- **ruim** (trechos faq-02, wiki-02): Não encontrei essa informação nas fontes disponíveis.

### q7. O que significa o código de erro E2 e como resolver?

Gabarito: E2 é pressão insuficiente. A causa comum é moagem grossa demais. A solução é usar moagem fina, parecida com açúcar refinado.

- **bom** (trechos manual-09, faq-06, faq-01): O código de erro E2 significa pressão insuficiente causada por moagem grossa demais, que deixa o café aguado. Para resolver, verifique a moagem e utilize uma moagem fina, parecida com açúcar refinado, evitando que seja grossa demais.
- **ruim** (trechos manual-01, manual-03): Não encontrei essa informação nas fontes disponíveis.

### q8. Qual é a capacidade do reservatório de água da Aurora K3?

Gabarito: Não há essa informação. A Aurora K3 foi anunciada para 2027 e nenhuma especificação foi divulgada.

- **bom** (trechos wiki-05, faq-10, manual-01): Não encontrei essa informação nas fontes disponíveis.
- **ruim** (trechos faq-10, manual-01): Não encontrei essa informação nas fontes disponíveis.

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
