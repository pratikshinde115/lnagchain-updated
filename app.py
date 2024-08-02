from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.llms import Ollama
from langchain_core.prompts  import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv(dotenv_path ='.env')

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
LANGCHAIN_API_KEY  = os.getenv('LANGCHAIN_API_KEY')
# export LANGCHAIN_TRACING_V2="true"


model = Ollama(model="llama3.1")
parser = StrOutputParser()
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Answer all questions to the best of your ability.",),
        ('user', 'Questions:{questions}')
    ]
)


# print(f'OPENAI_API_KEY :{OPENAI_API_KEY}')

chain = prompt | model | parser
res =chain.invoke({"questions":"who is criss herison"})

print(res)