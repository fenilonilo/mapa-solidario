import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np

# Adicione estilos CSS para personalizar a aparência da página
st.markdown("""
<style>
body {
    color: #fff;
    background-color: linear-gradient(to right, #0C0C0C, #4A4A4A);
    font-family: Times New Roman;
}
div[data-testid="stImage"] {
  width: 50%;
  margin: auto;
}
div[data-testid="stImage"] img  {
    border-radius: 25px;
    box-shadow: 10px 10px 5px grey;
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 50%;
    text-align: center;
}
h1 {
    text-align: center;
    font-family: Arial;
    font-size: 40px;
}
h4 {
    text-align: center;
    font-family: Arial;
    font-size: 20px;
}
div.stButton > button:first-child {
    display: block;
    margin: 0 auto;
    height: 80px;
    width: 200px;
    background-color: #4CAF50;
    color: white;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)


# Use o método st.markdown para renderizar o código HTML e CSS
st.image('Mapa Solidário Logo.png')

# Caminho para a imagem
st.markdown('<h1>Mapa Solidário</h1>', unsafe_allow_html=True)
st.markdown('<h4>Conectando Corações, Transformando Vidas</h4>', unsafe_allow_html=True)

# Dados para os blocos
dados = [
    {"titulo": "ONG 1", "descricao": "Descrição 1", "link": "https://www.bing.com"},
    {"titulo": "ONG 2", "descricao": "Descrição 2", "link": "https://www.microsoft.com"},
    {"titulo": "ONG 3", "descricao": "Descrição 3", "link": "https://www.microsoft.com"}
    # Adicione mais blocos conforme necessário
]

for bloco in dados:
    with st.expander(bloco["titulo"], expanded=False):
        st.write(bloco["descricao"])
        st.markdown(f"Participe: {bloco['link']}", unsafe_allow_html=True)