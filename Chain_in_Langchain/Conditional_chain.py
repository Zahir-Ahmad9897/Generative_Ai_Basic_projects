from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field 
from typing import Literal
from dotenv import load_dotenv
load_dotenv()


llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0)

# pydantic class

class Review_feedback(BaseModel):
    sentiment: Literal["positive", "negative"]
    review: str = Field(description="The review text")


# StrOutputParser
str_output_parser=StrOutputParser()

# Pydantic output_parsers

pydantic_output_parsers=PydanticOutputParser(pydantic_object=Review_feedback)


# ---------------**--------------


# classifier_prompt from_template
classifier_prompt=ChatPromptTemplate.from_messages([
    ("system", "you are best review classifier and you have to classify the review as positive or negative {format_instructions} \n"),
    ("human", "classify the review \n {review}")
])
# take output in specific formate
classifier_prompt=classifier_prompt.partial(format_instructions=pydantic_output_parsers.get_format_instructions())


# ---------------**--------------
# classifier chain
classifier_chain= classifier_prompt | llm | pydantic_output_parsers


# ---------------**--------------

# response prompts
#   take appropriate response for positive review

prompt2=ChatPromptTemplate.from_messages([
    ("system", "you are best reviewer"),
    ("human", "give best and suitable response to positive review \n {review}")
])

#   take appropriate response for negative review
prompt3=ChatPromptTemplate.from_messages([
    ("system", "you are best reviewer"),
    ("human", "give best and suitable response to negative review \n {review}")
])

# response chain
positive_review_chain=prompt2 | llm | str_output_parser
negative_review_chain=prompt3 | llm | str_output_parser


# ---------------**--------------

# Branching logic
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", positive_review_chain),
    (lambda x: x.sentiment == "negative", negative_review_chain),
    RunnableLambda(lambda x:" not found any review")
)

# ---------------**--------------

# merge the chain
final_chain = classifier_chain | branch_chain


# Test
text = "I love this product! It's amazing."
result = final_chain.invoke({"review": text})
print(result)
