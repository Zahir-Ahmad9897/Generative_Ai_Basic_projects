from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")
llm = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=groq_api_key)

parser = StrOutputParser()
prompt1 = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful ai  assistant and tutor."),
    ("human", "give me short helpfull notes on topic \n {text}")
])

prompt2 = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful ai  assistant."),
    ("human", "genrate 5 question on topic \n {text}")
])

prompt3 = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful ai  assistant."),
    ("human", "now merge my notes {notes} and quiz {question} into single Document ")
])
# use runnables for parallel excution

parallel_chain=RunnableParallel({
    'notes': prompt1 | llm | parser,
    'question': prompt2 | llm | parser
    
})

merge_chain= prompt3 | llm | parser

# Simple chain in langchain
final_chain = parallel_chain | merge_chain

text="D:\Gen AI_LANGChain\text.txt"
result = final_chain.invoke({"text": text })


print(result)