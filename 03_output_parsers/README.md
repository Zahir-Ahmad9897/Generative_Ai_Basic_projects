# Output Parsers

Learning how to get structured output from LLMs instead of raw text.

## What I Built

**Stroutput_parser.ipynb** - String Output Parser
- Built a chain with Groq's Llama 3.3-70b-versatile
- Used StrOutputParser to extract clean text from AI responses
- Tested on multiple topics: "langchain", "artificial intelligence", "machine learning"

Working chain:
```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant..."),
    ("user", "Tell me about {topic} in 2-3 sentences.")
])
chain = prompt | llm | StrOutputParser()
```

**Json_output_parser.ipynb** - JSON Output Parser
- Built a robust chain to get raw JSON responses from LLM
- Used `JsonOutputParser` to ensure output is valid JSON
- Learned the critical lesson: **Format instructions MUST be in the prompt** using `parser.get_format_instructions()`

**Structure_output_parser.ipynb** - Structured Output Parser (ResponseSchema)
- Implemented `StructuredOutputParser` using `ResponseSchema` objects
- Defined strict schemas for extracting specific data (name, age, gender)
- Learned how to use `from_response_schemas` for typed extraction
- Successfully extracted structured dictionaries from natural language text

## Critical Learning: The Format Instructions Problem

### What Went Wrong
Initially tried:
```python
parser = JsonOutputParser()
chain = prompt | llm | parser
result = chain.invoke({"topic": "cats"})
# ERROR: Invalid json output - got plain text!
```

The LLM returned:
```
"Here's a short summary about cats: Cats are small, carnivorous mammals..."
```

Parser expected JSON but got a paragraph.

### Why It Failed
The JsonOutputParser can only PARSE JSON - it cannot FORCE the LLM to generate JSON.  
The LLM needs explicit instructions in the prompt telling it to return JSON format.

### The Solution
```python
parser = JsonOutputParser(pydantic_object=Schema)
prompt = PromptTemplate(
    template="{format_instructions}\n\nTopic: {topic}",
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
```

## Key Insights

1. **StrOutputParser is simple** - Just extracts the text content from AIMessage
2. **JsonOutputParser is powerful** - Forces JSON structure via prompt instructions
3. **StructuredOutputParser is for complex schemas** - Uses `ResponseSchema` for multi-field extraction
4. **The parser doesn't control the LLM** - your prompt does
5. **Debugging parsing errors taught me more than success would have**

## String Parser Success

Ran the string parser on 3 topics and got clean, concise responses:
- "LangChain is an open-source framework that enables developers..."
- "Artificial intelligence (AI) refers to the development of computer systems..."
- "Machine learning is a subset of artificial intelligence..."

All outputs were clean strings, no extra AIMessage wrapping.

## Lessons Learned

The biggest lesson: **When working with output parsers, the prompt is everything.**

You can't just attach a parser and expect magic. The LLM needs to be explicitly told:
- What format to use
- What structure to follow  
- To return ONLY that format with no extra text

This debugging experience taught me more about how LangChain works than 10 successful examples would have.

## Examples Folder

Created additional complete examples in `/examples`:
- `json_parser_example.py` - With Pydantic schema
- `json_parser_simple.py` - Without schema
- `json_output_parser_complete.ipynb` - Full guide with all patterns

These contain the working solutions after learning from my mistakes.
