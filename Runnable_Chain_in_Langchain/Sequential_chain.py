from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")
llm = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=groq_api_key)

parser = StrOutputParser()

# create 3 prompt which gose to model sequentially
prompt1 = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful ai  assistant."),
    ("human", "give me detail explaination on topic {question}")
])

prompt2 = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful ai  assistant."),
    ("human", "give me 5 line summary on topic {question}")
])

prompt3 = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful ai  assistant."),
    ("human", "also add some conceptual part to it with proper heading 5 line summary on topic {question}")
])

# Simple chain in langchain
chain = prompt1 | llm | parser | prompt2 | llm | parser | prompt3 | llm | parser
result = chain.invoke({"question": "RNN"})


print(result)

# visuallize chain
chain.get_graph().print_ascii()
 
