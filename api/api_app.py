from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
import uvicorn
from langchain_community.llms import Ollama
from  dotenv import load_dotenv
from langserve import add_routes
from langchain_community.llms import Ollama

load_dotenv(dotenv_path ='../.env')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


app =FastAPI(
    title= "langchain server",
    version = '1.0',
    decsriptioon ="a simple api server"
)
add_routes(
    app,
    ChatOpenAI(),
    path='/ChatAi'
)
model = ChatOpenAI()

llm = Ollama(model = 'llama3.1')

prompt1 = ChatPromptTemplate.from_messages('write me a eaasy on 100 words whatever {topic} i give you')

prompt2 = ChatPromptTemplate.from_messages('write me a poem on 10 words whatever {topic} i give you')


add_routes(
    app,
    prompt1 | model ,
    path='/openai'
)

add_routes(
    app,
    prompt2 | llm,
    path='/llm'
)

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port = 8080)