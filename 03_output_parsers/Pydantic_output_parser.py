from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")
llm = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=groq_api_key)

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the person")
    gender: str = Field(description="Gender of the person")

parser = PydanticOutputParser(pydantic_object=Person)

# 2. Define the prompt template
prompt = ChatPromptTemplate.from_template(
    template="Answer the user query.\n{format_instructions}\nTopic: {topic}",
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# 3. Create and run the chain
chain = prompt | llm | parser
result = chain.invoke({"topic": "cricket champion"})


print(result)