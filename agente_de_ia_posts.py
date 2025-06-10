import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv(override=True)


OPENAI_KEY = os.getenv("API_KEY")

chat = ChatOpenAI(
    model_name = "gpt-4o-mini",
    openai_api_key = OPENAI_KEY,
    temperature=0.7

)

st.title("Ferramenta de Posts🚀")
conteudo = st.text_input("Conteúdo")
publico = st.text_input("Público-alvo")
tom = st.selectbox("Tom de voz", ["Amigável", "Profissional", "Urgente", "Divertida"])


template_prompt = '''
Você é um copywriter especialista. Gera:
1) Um carrosselde Instagram. Me devolva uma resposta em Markdow, separando os slides
do carrossel muito bem.
2) Uma descrição ótima.
conteudo: {conteudo}
Público-alvo: {publico}
Tom de voz: {tom}
'''

prompt = PromptTemplate.from_template(template_prompt)

if st.button("Gerar"):
    resposta = chat.invoke(prompt.format(conteudo = conteudo, publico = publico, tom = tom))
    st.subheader("Carrossel Instragram")
    st.write(resposta.content)
    