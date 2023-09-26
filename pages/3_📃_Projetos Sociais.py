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