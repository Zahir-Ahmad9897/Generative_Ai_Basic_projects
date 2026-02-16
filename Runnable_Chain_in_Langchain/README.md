# LangChain Expression Language (LCEL) Implementations

This module demonstrates the orchestration of Large Language Models (LLMs) using the LangChain Expression Language (LCEL). It provides production-level examples of chain composition, ranging from basic sequences to complex conditional branching logic.

## Overview

The implementations within this directory showcase how to build modular and maintainable AI workflows. By leveraging LCEL, these chains benefit from built-in support for async operations, batch processing, and streaming.

## Core Implementations

### Simple Chain
Basic orchestration of a prompt template, LLM integration, and output parsing. This serves as the fundamental building block for all other chain types.

### Sequential Chain
Demonstrates the execution of multiple components in a strict linear order. The output of the preceding component serves as the input for the succeeding one, enabling multi-step reasoning processes.

### Parallel Chain
Utilizes `RunnableParallel` to execute multiple independent tasks concurrently. This implementation is optimized for performance when retrieving diverse datasets or performing multiple analysis tasks on a single input.

### Lambda & Passthrough Chains
Demonstrates the use of `RunnableLambda` for custom Python function integration and `RunnablePassthrough` for data flow management. This implementation illustrates how to perform supplemental computations (like word counting) while maintaining the original LLM response within a parallel processing framework.

### Conditional Chain
Implements advanced decision-making logic using `RunnableBranch`. This chain dynamically routes inputs to specialized sub-chains based on real-time classification (e.g., sentiment analysis or intent detection).

## Technical Components

*   **Runnable Interface**: Utilization of `RunnablePassthrough` (identity function), `RunnableLambda` (custom Python logic), `RunnableParallel` (concurrent tasks), and `RunnableBranch` (decision logic).
*   **Prompt Engineering**: Implementation of `ChatPromptTemplate` with robust system instructions and partial variable injection.
*   **Validation**: Integration of `StrOutputParser` and `PydanticOutputParser` for flexible output handling.
*   **Providers**: Configuration with Groq (Llama 3.3) for high-speed inference.

## Usage

To execute a specific orchestration pattern, run the corresponding Python script:

```bash
python Simple_chain.py
python Sequential_chain.py
python Parallel_chain.py
python Conditional_chain.py
python Runnable_lembda.py
```

