import os
from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes

llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0.7)
prompt = ChatPromptTemplate.from_template("Tell me a short summry about {topic}")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

response = chain.invoke({"topic": "cats"})
print(response)

# fastapi app
app=FastAPI(title="Langchain Basics", 
            version="1.0.0",
            description="A simple API for Langchain Basics")

add_routes(app, chain, path="/joke")

# run the app
# uvicorn serve:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)