import requests 
import streamlit as st 

def get_openai_responce(input_text):
    responce = requests.post("http://localhost:8080/openai/invoke",
    json= {'input':{'topic':input_text}})


    return responce.json()

def get_llm_responce(input_text):
    responce = requests.post("http://localhost:8080/llm/invoke",
    json= {'input':{'topic':input_text}})

   
    return responce.json()['output']



st.title('Langchain Demo With Lamma APi')
input_text = st.text_input("write a poem")


if input_text:
    st.write(get_llm_responce(input_text))