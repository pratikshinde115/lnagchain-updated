from langchain_community.document_loaders import TextLoader , WebBaseLoader , PyPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings , OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain.chains.combine_documents import create_stuff_documents_chain
import bs4
from langchain.chains import create_retrieval_chain

from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv  
import os

from langchain_community.llms import Ollama

load_dotenv(dotenv_path ='../.env')


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


# txt_loader
loader = TextLoader('../Document/lstm.txt',encoding='utf-8')
# loader.load()

# webscraping
loader = WebBaseLoader(web_path= ('https://colah.github.io/posts/2015-08-Understanding-LSTMs/',),
    bs_kwargs = dict(parse_only =bs4.SoupStrainer(
        class_ = "col-md-8"
    )))

# print(loader.load())

# pdf_loader


loader = PyPDFLoader('../Document/LSTM.pdf')

# print(loader.load())
pdf_doc=loader.load()

# chunk

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
docs =text_splitter.split_documents(pdf_doc)

print(docs[0])

db = Chroma.from_documents(docs,OllamaEmbeddings(model ='llama3.1'))

# querry = 'The Problem of lstm'

# result = db.similarity_search(querry)

# print(result)
prompt = ChatPromptTemplate.from_template(
    """
    answer the following question 
    {context}
    Question :{input}
    """
)

# create_stuff_documents_chain

## Load Ollama LAMA2 LLM model
llm=Ollama(model ='llama3.1')
llm
document_chain = create_stuff_documents_chain(llm,prompt)
retriever=db.as_retriever()
retriever
retrieval_chain=create_retrieval_chain(retriever,document_chain)

responce=retrieval_chain.invoke({"input":"how lstm solves rnn problem"})

responce['answer']