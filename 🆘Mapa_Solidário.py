from collections import namedtuple
import math
import pandas as pd
import streamlit as st
import time
from tools.Localizacao import Localizacao

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

# Crie um espaço vazio para alinhar o botão 'Help' no centro da página
st.write("\n\n\n\n")

# Defina o estado inicial do botão 'Help'
if "help_clicked" not in st.session_state:
    st.session_state["help_clicked"] = False

# Crie o botão 'Help' no centro da página
if st.button('Help'):
    st.session_state["help_clicked"] = True

# Crie um espaço reservado para a mensagem do botão 'Help'
help_text = st.empty()

# Se o botão 'Help' foi clicado, exiba a mensagem e depois apague-a
if st.session_state["help_clicked"]:
    Localizacao.pegar_localizacao()
    help_text.markdown("<h3 style='text-align: center; font-family: Georgia;'>Localização Coletada!\n\t\t ✅</h3>", unsafe_allow_html=True)
    time.sleep(2)
    help_text.empty()

# Adicione um texto "Clique aqui para obter ajuda" abaixo do botão 'Help' usando HTML
st.markdown('<p style="text-align: center; font-family: Arial; font-size: 15px;">Clique aqui para obter ajuda</p>', unsafe_allow_html=True)

# Adicione um ícone de coração ao lado do botão 'Help' usando HTML
st.markdown('<p style="text-align: center;"><span style="font-size: 40px; color: red;">&#10084;</span></p>', unsafe_allow_html=True)