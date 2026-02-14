# Chat Models

Explored different LLM providers and how to integrate them with LangChain.

## What I Built

**ChatModel_1.ipynb** - HuggingFace Integration
- Integrated Intel's neural-chat-7b-v3-1 from HuggingFace
- Set up proper tokenizer configuration
- Built two approaches:
  1. Direct messages with SystemMessage/HumanMessage
  2. ChatPromptTemplate for reusable prompts

### Example 1: French Translation
Asked the model to translate "Hello, I am fine, how are you?" into French.  
Got back: "Bonjour, je suis bien, comment allez-vous ?"

### Example 2: AI Professor Chain
Created a chain that explains technical concepts in simple English.  
Template: "You are a helpful ai professor. Please explain '{text}' in easy english"

## Key Learnings

**HuggingFace requires tokenizer setup**
```python
tokenizer = AutoTokenizer.from_pretrained("Intel/neural-chat-7b-v3-1")
chat = ChatHuggingFace(llm=llm, tokenizer=tokenizer)
```

**Two ways to use chat models:**
1. Direct: `chat.invoke([SystemMessage(...), HumanMessage(...)])`
2. With template: `template | chat | parser`

**API token management matters** - Loaded from `.env` file for security

## Challenges

- Initially forgot to set up tokenizer - got errors
- Learned that different models need different configurations
- HuggingFace models are slower than Groq but free to use

## Working Example

The actual chain I built:
```python
chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful ai professor."),
    HumanMessage(content="Please explain '{text}' in easy english")
])
chain = chat_template | chat
response = chain.invoke({"text": "what is langchain"})
```

This taught me how to create reusable prompt templates with variables.

## Models Tested

- **Intel/neural-chat-7b-v3-1** (HuggingFace) - Works well for explanations
- **Groq/Llama-3.1-8b** - Much faster, used in other notebooks
- Learned how to switch between providers by changing the chat model initialization
