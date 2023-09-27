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
    font-size: 13px;
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

descricao_1 = '''
A ONG Anjos da Cidade dedica seus esforços à assistência de moradores de rua,
fornecendo refeições,
abrigo e apoio com o objetivo de melhorar suas condições de vida e reintegrá-los à sociedade.
'''

descricao_2 = '''
A ONG Liiga do Bem concentra sua atenção em oferecer
apoio abrigo e programas de reintegração social para moradores de rua,
com a finalidade de melhorar suas vidas e facilitar sua inclusão na sociedade.
'''

descricao_3 = '''
A Associação Tio Cleobaldo, sediada em Goiânia, Goiás,
distribui refeições para moradores de rua há mais de 40 anos,
contando com doações para sua operação. Seu objetivo é reduzir a vulnerabilidade,
restaurando a dignidade e reintegrando essas pessoas à sociedade. 
Além disso, oferecem apoio a crianças, gestantes e famílias em situação de rua.
'''

# Dados para os blocos
dados = [
    {"titulo": "Anjos da Cidade", "descricao": f"{descricao_1}", "link": "https://www.anjosdacidade.org/"},
    {"titulo": "Liiga do Bem", "descricao": f"{descricao_2}", "link": "https://coepbrasil.org.br/fome-ong-liiga-do-bem/"},
    {"titulo": "Associação Tio Cleobaldo", "descricao": f"{descricao_3}", "link": "https://transformabrasil.com.br/projeto/associacao-do-tio-cleobaldo"}
    # Adicione mais blocos conforme necessário
]

for bloco in dados:
    with st.expander(bloco["titulo"], expanded=False):
        st.write(bloco["descricao"])
        st.markdown(f"Participe: {bloco['link']}", unsafe_allow_html=True)