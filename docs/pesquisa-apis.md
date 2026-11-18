# Pesquisa: APIs atuais de Ragas, DeepEval e Promptfoo

Data da consulta: 18/11/2026.
Método: WebFetch nas docs oficiais e nos registros (PyPI, npm). Para tirar dúvida, baixei os pacotes `ragas==0.4.4` e `deepeval==4.3.4` (wheel, sem instalar) e li o código-fonte. Itens vindos só do código estão marcados "(código)".
Marca "NÃO CONFIRMADO" = não achei na doc, estou deduzindo.

## Resumo rápido

| Ferramenta | Versão | Data | Requisito |
|---|---|---|---|
| ragas (PyPI) | 0.4.4 | 14/11/2026 | Python >= 3.9 |
| deepeval (PyPI) | 4.3.4 | 11/11/2026 | Python >= 3.10, < 4.0 |
| promptfoo (npm) | 0.125.1 | data NÃO CONFIRMADO | Node >= 22.22.0 |

Armadilhas principais:

1. Ragas 0.4 tem DUAS APIs. A "collections" (`ragas.metrics.collections`) é a recomendada, mas NÃO funciona em `evaluate()`. A legada (`ragas.metrics`) funciona em `evaluate()`, mas está marcada como deprecated no 0.4 e removida no 1.0.
2. Ragas `ContextPrecision` (nos dois módulos) exige `reference`. A variante sem referência é `LLMContextPrecisionWithoutReference` (legada) ou `ContextPrecisionWithoutReference` / `ContextUtilization` (collections).
3. Ragas: `ResponseRelevancy` (legada) virou `AnswerRelevancy` na API collections. Na legada, `AnswerRelevancy` é subclasse de `ResponseRelevancy`.
4. DeepEval: `GPTModel` foi renomeada para `OpenAIModel` (`GPTModel` ainda existe, com aviso de deprecated). `OpenAIModel` aceita `base_url`.
5. DeepEval: `ContextualPrecisionMetric` e `ContextualRecallMetric` exigem `expected_output`.
6. Promptfoo: `context-recall` exige `value` (resposta de referência). `context-faithfulness` e `context-relevance` exigem as vars `query` e `context`.
7. Promptfoo: `answer-relevance` usa também um provider de embeddings. Se o endpoint compatível não tiver embeddings, configure `defaultTest.options.provider.embedding`.

---

## 1. Ragas

Páginas consultadas:
- https://pypi.org/project/ragas/
- https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/
- https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/
- https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/answer_relevance/
- https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/
- https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_recall/
- https://docs.ragas.io/en/stable/getstarted/rag_eval/
- https://docs.ragas.io/en/stable/getstarted/quickstart/
- https://docs.ragas.io/en/stable/howtos/customizations/customize_models/
- https://docs.ragas.io/en/stable/references/evaluate/
- Código: https://raw.githubusercontent.com/vibrantlabsai/ragas/main/src/ragas/llms/base.py, `.../evaluation.py`, `.../metrics/collections/__init__.py`, `.../metrics/collections/base.py`
- Wheel `ragas-0.4.4-py3-none-any.whl` (PyPI), lido localmente.

### 1.1 Versão

`ragas` 0.4.4, lançada em 14/11/2026. Python >= 3.9.

### 1.2 Duas APIs (leia antes de escolher)

| | Collections (recomendada) | Legada (deprecated no 0.4, removida no 1.0) |
|---|---|---|
| Import das métricas | `from ragas.metrics.collections import ...` | `from ragas.metrics import ...` |
| Dataset | argumentos soltos em `ascore(...)` / `score(...)` | `SingleTurnSample`, `EvaluationDataset` |
| Chamada | `await m.ascore(...)` ou `m.score(...)` -> `result.value` | `await m.single_turn_ascore(sample)` ou `evaluate(...)` |
| Funciona em `evaluate()` | NÃO (código) | SIM |

Prova no código (0.4.4): `evaluate()` faz `isinstance(m, Metric)` e lança `TypeError` se não for. As métricas collections herdam de `SimpleBaseMetric`, que NÃO herda de `Metric` (`metrics/base.py`, linhas 75 e 689). Logo `evaluate(metrics=[collections.Faithfulness(...)])` falha com `TypeError` (dedução a partir do código; não rodei).

`evaluate()` também emite `DeprecationWarning`: "evaluate() is deprecated and will be removed in a future version. Use the @experiment decorator instead." (código).

Consequência: para ter `evaluate(...)` + `to_pandas()` por linha, use a API legada. Para evitar código deprecated, use a collections e faça o laço você mesmo.

### 1.3 Dataset de amostra única

Legado (usado com `evaluate`):

```python
from ragas import EvaluationDataset
from ragas.dataset_schema import SingleTurnSample

sample = SingleTurnSample(
    user_input="When was the first super bowl?",
    response="The first superbowl was held on Jan 15, 1967",
    retrieved_contexts=["The First AFL–NFL World Championship Game was ... January 15, 1967 ..."],
    reference="The first Super Bowl was held on January 15, 1967.",
)
```

Campos de `SingleTurnSample` (código): `user_input`, `retrieved_contexts`, `reference_contexts`, `retrieved_context_ids`, `reference_context_ids`, `response`, `multi_responses`, `reference`, `rubric`, `persona_name`.

Dataset a partir de lista de dicts (copiado da doc "rag_eval"):

```python
from ragas import EvaluationDataset
evaluation_dataset = EvaluationDataset.from_list(dataset)  # lista de dicts com user_input, retrieved_contexts, response, reference
```

Nota: a doc usa `from ragas import SingleTurnSample` em alguns lugares e `from ragas.dataset_schema import SingleTurnSample` em outros. Usei o segundo, que está no código-fonte.

### 1.4 LLM juiz com endpoint compatível com OpenAI

#### A) API nova: `llm_factory` (recomendada)

Assinatura (código, `llms/base.py`):

```python
def llm_factory(model: str, provider: str = "openai", client=None, adapter: str = "auto",
                cache=None, mode=None, **kwargs) -> InstructorBaseRagasLLM
```

- `client` é obrigatório (sem ele: `ValueError`).
- NÃO existe parâmetro `base_url` em `llm_factory`. O `base_url` vai no cliente OpenAI.

Exemplo da doc (quickstart, Ollama), com `base_url` e `api_key` customizados:

```python
from openai import OpenAI
from ragas.llms import llm_factory

client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1",
)
llm = llm_factory("mistral", provider="openai", client=client)
```

Para métricas collections, a doc usa `AsyncOpenAI` (`client = AsyncOpenAI(); llm = llm_factory("gpt-4o-mini", client=client)`). Com endpoint próprio: `AsyncOpenAI(api_key=..., base_url=...)` (dedução; NÃO CONFIRMADO que a doc mostre esse par exato).

Embeddings (doc `answer_relevance`):

```python
from ragas.embeddings.base import embedding_factory
embeddings = embedding_factory("openai", model="text-embedding-3-small", client=client)
```

Assinatura (código): `embedding_factory(provider="openai", model=None, run_config=None, client=None, interface="auto", base_url=None, cache=None, **kwargs)`. Aqui existe `base_url`.

#### B) API legada: wrappers do LangChain (necessária para `evaluate()` com garantia)

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper

evaluator_llm = LangchainLLMWrapper(ChatOpenAI(model="...", base_url="...", api_key="..."))
evaluator_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings(model="...", base_url="...", api_key="..."))
```

- `LangchainLLMWrapper` e `LangchainEmbeddingsWrapper` existem no 0.4.4. `LangchainLLMWrapper` emite `DeprecationWarning` ("deprecated and will be removed in a future version", aponta para `llm_factory`) (código).
- A doc "rag_eval" mostra só `LangchainLLMWrapper(ChatOpenAI(model="gpt-4o"))`, sem `base_url`. Os parâmetros `base_url`/`api_key` de `ChatOpenAI`/`OpenAIEmbeddings` são do `langchain_openai`, não da doc do Ragas. NÃO CONFIRMADO na doc do Ragas.
- `evaluate()` aceita `llm=` e `embeddings=` e envolve objetos LangChain sozinho (código: `isinstance(llm, LangchainLLM)` -> `LangchainLLMWrapper`).
- Se `llm_factory` (Instructor) funciona com métricas legadas dentro de `evaluate()`: a assinatura de `evaluate` aceita `InstructorBaseRagasLLM`, mas não testei com métricas legadas. NÃO CONFIRMADO.
- Sem `llm=`, `evaluate()` cai em `OpenAI()` + `gpt-4o-mini` (código). Sempre passe `llm=`.

### 1.5 Métricas

| Métrica | API collections | API legada | Campos exigidos | Exige `reference`? |
|---|---|---|---|---|
| Faithfulness | `Faithfulness` | `Faithfulness` | user_input, response, retrieved_contexts | Não |
| Relevância da resposta | `AnswerRelevancy` | `ResponseRelevancy` (e `AnswerRelevancy`, subclasse) | user_input, response (+ embeddings) | Não |
| Context Precision (sem referência) | `ContextPrecisionWithoutReference`, `ContextUtilization` | `LLMContextPrecisionWithoutReference` (e `ContextUtilization`) | user_input, response, retrieved_contexts | Não |
| Context Precision (com referência) | `ContextPrecision` | `LLMContextPrecisionWithReference`, `ContextPrecision` (alias) | user_input, reference, retrieved_contexts | SIM |
| Context Recall | `ContextRecall` | `LLMContextRecall` | user_input, retrieved_contexts, reference | SIM |

Detalhes:
- Collections: `ContextPrecision` "needs a reference answer" (doc). `ContextUtilization` não precisa. As classes `ContextPrecisionWithReference` e `ContextPrecisionWithoutReference` estão em `__all__` de `ragas.metrics.collections` (código); a doc só descreve `ContextPrecision` e `ContextUtilization`.
- Legado: os campos acima vêm da doc de `context_precision` e do `_required_columns` no código.
- `AnswerRelevancy` calcula similaridade de cosseno entre a pergunta e perguntas geradas: exige embeddings.
- Variantes sem LLM (legadas): `NonLLMContextRecall` e `NonLLMContextPrecisionWithReference` usam `reference_contexts` (não `reference`); `IDBased*` usam IDs.
- Nome da coluna no resultado (código): `faithfulness`, `answer_relevancy`, `llm_context_precision_without_reference`, `llm_context_precision_with_reference`, `context_precision` (classe alias), `context_utilization`, `context_recall`. `LLMContextRecall` tem `name = "context_recall"`.

### 1.6 Uso com métricas collections (sem `evaluate`)

Copiado/adaptado da doc de Faithfulness:

```python
from openai import AsyncOpenAI
from ragas.llms import llm_factory
from ragas.metrics.collections import Faithfulness

client = AsyncOpenAI()  # com endpoint próprio: AsyncOpenAI(api_key=..., base_url=...)
llm = llm_factory("gpt-4o-mini", client=client)
scorer = Faithfulness(llm=llm)

result = await scorer.ascore(
    user_input="When was the first super bowl?",
    response="The first superbowl was held on Jan 15, 1967",
    retrieved_contexts=["The First AFL–NFL World Championship Game ... January 15, 1967 ..."],
)
print(result.value)   # 1.0
```

Versão síncrona: `scorer.score(...)` (doc).
Relevância da resposta:

```python
from ragas.metrics.collections import AnswerRelevancy
scorer = AnswerRelevancy(llm=llm, embeddings=embeddings)
result = await scorer.ascore(user_input="...", response="...")
```

### 1.7 `evaluate(...)` e resultado por linha (API legada)

Doc "rag_eval" (copiado):

```python
from ragas import evaluate
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import LLMContextRecall, Faithfulness, FactualCorrectness

evaluator_llm = LangchainLLMWrapper(llm)
result = evaluate(
    dataset=evaluation_dataset,
    metrics=[LLMContextRecall(), Faithfulness(), FactualCorrectness()],
    llm=evaluator_llm,
)
```

Assinatura (doc de referência): `evaluate(dataset, metrics=None, llm=None, embeddings=None, experiment_name=None, callbacks=None, run_config=None, token_usage_parser=None, raise_exceptions=False, column_map=None, show_progress=True, batch_size=None, ..., allow_nest_asyncio=True) -> EvaluationResult`.

- `raise_exceptions=False` (padrão): linha que falha vira `NaN`, sem erro. Use `True` ao depurar.
- Resultado por linha: `result.to_pandas()` (código: `EvaluationResult.to_pandas(batch_size=None, batched=False)`). O `print(result)` mostra a média por métrica, ex. `{'context_recall': 1.0000, 'faithfulness': 0.8571, ...}`. `result["faithfulness"]` devolve a lista por linha (código: `__getitem__`).
- A página "rag_eval" da doc NÃO mostra `to_pandas`; ele só está no código-fonte. A doc de referência também não lista os métodos de `EvaluationResult`.

---

## 2. DeepEval

Páginas consultadas:
- https://pypi.org/project/deepeval/
- https://deepeval.com/docs/metrics-faithfulness
- https://deepeval.com/docs/metrics-answer-relevancy
- https://deepeval.com/docs/metrics-contextual-precision
- https://deepeval.com/docs/metrics-contextual-recall
- https://deepeval.com/docs/metrics-introduction
- https://deepeval.com/docs/evaluation-introduction
- https://deepeval.com/guides/guides-using-custom-llms
- https://deepeval.com/integrations/models/openai
- Wheel `deepeval-4.3.4-py3-none-any.whl` (PyPI), lido localmente.

### 2.1 Versão

`deepeval` 4.3.4, lançada em 11/11/2026. Python >= 3.10, < 4.0.

### 2.2 `LLMTestCase`

```python
from deepeval.test_case import LLMTestCase

test_case = LLMTestCase(
    input="What if these shoes don't fit?",
    actual_output="We offer a 30-day full refund at no extra cost.",
    expected_output="You are eligible for a 30-day full refund at no extra cost.",
    retrieval_context=["All customers are eligible for a 30-day full refund at no extra cost."],
)
```

`retrieval_context` é lista de strings. A doc não traz a lista completa de campos; ela remete a https://deepeval.com/docs/evaluation-test-cases (não consultei). O código tem também `context` (campo diferente de `retrieval_context`).

### 2.3 Métricas e campos exigidos

Import: `from deepeval.metrics import FaithfulnessMetric, AnswerRelevancyMetric, ContextualPrecisionMetric, ContextualRecallMetric`.

| Métrica | input | actual_output | retrieval_context | expected_output |
|---|---|---|---|---|
| `FaithfulnessMetric` | sim | sim | sim | não |
| `AnswerRelevancyMetric` | sim | sim | não | não |
| `ContextualPrecisionMetric` | sim | sim | sim | SIM |
| `ContextualRecallMetric` | sim | sim | sim | SIM |

Parâmetros comuns (docs): `threshold` (padrão 0.5; `None` = só pontuação), `model` (nome OpenAI ou `DeepEvalBaseLLM`), `include_reason` (True), `strict_mode` (False; força 0/1 e threshold 1), `async_mode` (True), `verbose_mode` (False). Nas docs de AnswerRelevancy e Contextual* há ainda `evaluation_template`, `flaky`, `system_one_model`, `eval_mode` (`llm`, `hybrid`, `system_one`).

Uso individual (doc):

```python
metric = AnswerRelevancyMetric(threshold=0.7, model="gpt-4.1", include_reason=True)
metric.measure(test_case)
print(metric.score, metric.reason)
```

`metric.is_successful()` diz se passou do threshold (doc de introdução).

### 2.4 Modelo customizado com endpoint compatível com OpenAI

Há três caminhos.

**A) `OpenAIModel` com `base_url` (doc + código).** A doc de integração chama a classe `OpenAIModel`, não `GPTModel`. Parâmetros: `model`, `api_key`, `base_url`, `temperature`, `cost_per_input_token`, `cost_per_output_token`, `generation_kwargs`.

```python
from deepeval.models import OpenAIModel

judge = OpenAIModel(
    model="gpt-4.1",
    temperature=0,
    cost_per_input_token=0.000002,
    cost_per_output_token=0.000008,
    # base_url="https://meu-endpoint/v1", api_key="..."   # parâmetros existem na assinatura (código e doc)
)
metric = FaithfulnessMetric(model=judge)
```

- O exemplo da doc não mostra `base_url`/`api_key` juntos; eles só estão na lista de parâmetros. Montei a chamada a partir dela.
- `from deepeval.models import GPTModel` ainda funciona em 4.3.4, mas chama `warn_gpt_model_deprecated()` e devolve `OpenAIModel` (código).
- Modelo com nome fora do catálogo do DeepEval: o código chama `require_costs(...)`. Se ele exige `cost_per_input_token` e `cost_per_output_token` para nomes desconhecidos: NÃO CONFIRMADO. Por segurança, passe os dois custos.

**B) CLI `deepeval set-local-model` (só no código; a doc de introdução não citou).** Opções: `--model/-m`, `--base-url/-u`, `--prompt-api-key/-k`, `--format/-f` (padrão json), `--save/-s` (grava em dotenv). Variáveis: `LOCAL_MODEL_NAME`, `LOCAL_MODEL_BASE_URL`, `LOCAL_MODEL_API_KEY`, `LOCAL_MODEL_FORMAT`. Desfaz com `deepeval unset-local-model`. Não achei página da doc que descreva isso. Não rodei.

**C) Subclasse de `DeepEvalBaseLLM` (doc).** Métodos obrigatórios: `load_model()`, `generate(prompt, schema=None)`, `a_generate(prompt, schema=None)`, `get_model_name()`. Quando `schema` (Pydantic) é passado, o método deve devolver uma instância do schema. Sem isso, `FaithfulnessMetric` falha com `AttributeError` confuso. Modelos pequenos erram JSON; a doc recomenda `instructor` ou `lm-format-enforcer`. Exemplo completo: https://deepeval.com/guides/guides-using-custom-llms (não copiei; texto longo).

**`deepeval set-openai`:** a doc de integração mostra `deepeval set-openai --model=gpt-4.1 --cost-per-input-token=... --cost-per-output-token=...` (`--save` persiste). Ela NÃO mostra opção de base URL nesse comando. Para endpoint próprio, use A, B ou C. Variáveis de ambiente na doc: `OPENAI_API_KEY`, `OPENAI_MODEL_NAME`, `TEMPERATURE`, `OPENAI_COST_PER_INPUT_TOKEN`, `OPENAI_COST_PER_OUTPUT_TOKEN`. O DeepEval lê `.env.local` e depois `.env` ao importar.

### 2.5 `evaluate(...)` em script, sem pytest

Doc (copiado):

```python
from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

evaluate(test_cases=[test_case], metrics=[metric])
```

Assinatura (código): `evaluate(test_cases, metrics=None, classifiers=None, metric_collection=None, hyperparameters=None, mcp_servers=None, identifier=None, official=False, async_config=AsyncConfig(), display_config=DisplayConfig(), cache_config=CacheConfig(), error_config=ErrorConfig()) -> EvaluationResult`.

Ler os scores. A doc NÃO documenta o retorno. No código (`evaluate/types.py`, `tracing/api.py`):

```python
result = evaluate(test_cases=[test_case], metrics=[metric])
for tr in result.test_results:          # EvaluationResult.test_results: List[TestResult]
    for md in tr.metrics_data:          # MetricData: name, score, threshold, success, reason, error
        print(md.name, md.score, md.success, md.reason)
```

Alternativa documentada: `metric.measure(test_case)` e depois `metric.score` / `metric.reason`.

Notas:
- Sem login na Confident AI o `evaluate` ainda deve rodar local. NÃO CONFIRMADO (não executei).
- Métrica com `threshold=None` só pontua e não entra no pass/fail (doc).

---

## 3. Promptfoo

Páginas consultadas:
- https://registry.npmjs.org/promptfoo/latest (versão e engines)
- https://www.promptfoo.dev/docs/providers/echo/
- https://www.promptfoo.dev/docs/providers/python/
- https://www.promptfoo.dev/docs/providers/openai/
- https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/
- https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/context-faithfulness/
- https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/context-relevance/
- https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/context-recall/
- https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/answer-relevance/
- https://www.promptfoo.dev/docs/configuration/outputs/
- A página https://www.npmjs.com/package/promptfoo devolveu 403.

### 3.1 Versão

`promptfoo` 0.125.1 (npm registry, `latest`). Exige Node >= 22.22.0. Data de publicação: NÃO CONFIRMADO.

### 3.2 Avaliar respostas já geradas, sem gerar

Caminho mais simples (doc do provider `echo`): o `echo` devolve o prompt renderizado como saída, sem chamar API. Ponha a resposta pronta numa var e use `{{var}}` como prompt. A doc cita esse uso: "Use `{{logged_output}}` as the prompt with `echo` as the provider" para avaliar saídas já logadas.

```yaml
# promptfooconfig.yaml
description: "Avaliar respostas RAG já geradas"
prompts:
  - "{{response}}"
providers:
  - echo
tests:
  - vars:
      query: "Who created Python?"
      response: "Python was created by Guido van Rossum in 1991."
      context:
        - "Guido van Rossum created Python in 1991."
    assert:
      - type: context-faithfulness
        threshold: 0.8
```

A estrutura `prompts` + `providers: [echo]` + `tests[].vars` vem da doc do `echo`. O YAML completo acima com `{{response}}` é dedução direta. NÃO CONFIRMADO por execução.

Alternativa `file://` com Python (doc do provider Python): `file://my_provider.py` (opcional `:funcao`), função `call_api(prompt: str, options: dict, context: dict) -> dict` devolvendo `{"output": ...}` ou `{"error": ...}`. A doc usa `file://`; o prefixo `python:` NÃO apareceu nessa página. Alternativa `exec:` NÃO consultada.

```yaml
providers:
  - id: 'file://my_provider.py'
    label: 'respostas-prontas'
```

Se o provider devolver um objeto com `answer` e `context`, use `contextTransform` (ver 3.3).

### 3.3 Asserts model-graded para RAG

Todos aceitam `threshold` (0 a 1, padrão 0.5) e `provider` (grader do assert).

| Assert | Vars/valores exigidos | Observação |
|---|---|---|
| `context-faithfulness` | vars `query` e `context` | A saída (output) é a resposta avaliada. |
| `context-relevance` | vars `query` e `context` | Não usa a resposta. |
| `context-recall` | `value` = resposta de referência (obrigatório); `context` em var ou `contextTransform` | Se `context` faltar, a doc diz que o prompt vira o contexto. |
| `answer-relevance` | a doc não nomeia a var; compara a saída com a pergunta original | Usa provider de embeddings além do de texto. Var `query`: NÃO CONFIRMADO. |

Exemplos copiados das docs:

```yaml
tests:
  - vars:
      query: 'What is the capital of France?'
      context: 'Paris is the capital and largest city of France.'
    assert:
      - type: context-faithfulness
        threshold: 0.9
```

`context` pode ser lista de strings (doc de context-faithfulness e context-relevance):

```yaml
vars:
  context:
    - 'Paris is the capital and largest city of France.'
    - 'France is located in Western Europe.'
```

```yaml
assert:
  - type: context-recall
    value: 'Python was created by Guido van Rossum in 1991'
    threshold: 1.0
```

```yaml
assert:
  - type: answer-relevance
    threshold: 0.7
```

Contexto vindo do provider: `contextTransform: 'output.context'` (ou `'output.chunks'` para lista).

### 3.4 Grader em endpoint compatível com OpenAI

Três formas de trocar o grader (doc model-graded):
1. CLI: `promptfoo eval --grader openai:gpt-6-sol`
2. `defaultTest.options.provider`
3. `provider` dentro de um assert

Exemplo da doc para endpoint próprio:

```yaml
defaultTest:
  options:
    provider:
      id: openai:chat:llm_judge
      config:
        apiBaseUrl: http://localhost:8000/v1
        apiKey: empty
        temperature: 0
```

Separar texto e embeddings (a doc mostra o formato `text`/`embedding` com Azure):

```yaml
defaultTest:
  options:
    provider:
      text:
        id: openai:chat:MODELO
        config: { apiBaseUrl: https://meu-endpoint/v1, apiKey: ... }
      embedding:
        id: openai:embedding:MODELO-EMB
        config: { apiBaseUrl: https://meu-endpoint/v1, apiKey: ... }
```

O trecho acima troca Azure por `openai:`. É dedução. NÃO CONFIRMADO que a doc mostre esse par exato.

Variáveis de ambiente (doc do provider OpenAI):
- `OPENAI_API_KEY`: chave padrão.
- `OPENAI_BASE_URL` e `OPENAI_API_BASE_URL`: URL base completa (`OPENAI_API_BASE_URL` tem preferência no mesmo nível). `OPENAI_API_HOST` monta `https://<host>/v1` e é checado antes.
- Ordem: `config.apiHost`, depois `config.apiBaseUrl`, depois variáveis de ambiente.
- Que o grader padrão herda essas variáveis: a doc de model-graded não afirma. NÃO CONFIRMADO.

IDs: `openai:chat:<modelo>` usa Chat Completions. Em gateway, use o ID do modelo exatamente como o gateway lista. Embeddings: `openai:embedding:<modelo>`; sem modelo, o padrão é `text-embedding-3-large`.

### 3.5 Exportar JSON

```bash
promptfoo eval -c promptfooconfig.yaml --output results.json
```

- A doc de outputs usa só `--output` (também `.csv`, `.yaml`, `.html`, `.jsonl`, `.junit.xml`, `.xml`). O atalho `-o` NÃO aparece nessa página: NÃO CONFIRMADO.
- Formato do JSON segundo a doc: topo com `version`, `timestamp`, `results`; dentro de `results`: `prompts`, `providers`, `outputs`, `stats`. A doc descreve `gradingResult` com `componentResults[]` (cada um com `pass`, `score`, `reason`) só para JSONL. O caminho `results.results[]` NÃO foi confirmado. Abra um `results.json` real antes de escrever o parser.
- Para parsing por linha, JSONL (`--output results.jsonl`) tem campos documentados: `success`, `score`, `gradingResult.componentResults`.

---

## 4. Pendências para testar na prática

- [ ] Ragas: rodar `evaluate()` com `LangchainLLMWrapper(ChatOpenAI(base_url=...))` e conferir `to_pandas()`.
- [ ] Ragas: confirmar que `evaluate()` recusa métricas collections (esperado: `TypeError`).
- [ ] Ragas: testar `llm_factory(...)` dentro de `evaluate()` com métricas legadas.
- [ ] DeepEval: criar `OpenAIModel(base_url=..., api_key=...)` com nome de modelo fora do catálogo e ver se pede custos.
- [ ] DeepEval: confirmar o formato de `result.test_results[].metrics_data[]`.
- [ ] Promptfoo: rodar `echo` com `{{response}}` e abrir o `results.json` real.
- [ ] Promptfoo: confirmar se o grader respeita `OPENAI_BASE_URL`.
