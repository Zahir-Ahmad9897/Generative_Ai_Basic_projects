from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")
llm = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=groq_api_key)

parser = StrOutputParser()
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful ai  assistant."),
    ("human", "give me 5 line summary on topic {question}")
])

# Simple chain in langchain
chain = prompt | llm | parser
result = chain.invoke({"question": "RNN"})


print(result)