import streamlit as st
import streamlit_folium as sf
import pandas as pd
import numpy as np
import folium
import altair as alt
from streamlit import components
import os 
import math
from branca.element import IFrame

st.markdown("<h1 style='text-align: center;'>Disposição dos Moradores de Rua</h1>", unsafe_allow_html=True)
DTYPE = {'latitude':float, 'longitude':float}
df = pd.read_csv('./pages/DataSet.csv',index_col=False,dtype=DTYPE)

# Define o centro da cidade
center_lat = -16.6869
center_lon = -49.2648

# Calcule a distância entre cada ponto e o centro da cidade
df['Distancia'] = np.sqrt((df['latitude'] - center_lat) ** 2 + (df['longitude'] - center_lon) ** 2)

# Define os setores
sectors = ['Central', 'Sul', 'Sudoeste', 'Sudeste', 'Norte', 'Noroeste', 'Nordeste']

# Crie uma variável categórica para os setores e defina as categorias
df['Setor'] = pd.Categorical(df['latitude'], categories=sectors)

# Definir o limite para o setor central
center_threshold = 0.02

# Atribuir cada ponto a um setor com base em sua distância do centro e sua posição relativa
df.loc[df['Distancia'] <= center_threshold, 'Setor'] = 'Central'
df.loc[(df['Setor'].isnull()) & (df['latitude'] < center_lat), 'Setor'] = 'Sul'
df.loc[(df['Setor'].isnull()) & (df['latitude'] > center_lat), 'Setor'] = 'Norte'
df.loc[(df['Setor'] == 'Sul') & (df['longitude'] < center_lon), 'Setor'] = 'Sudoeste'
df.loc[(df['Setor'] == 'Sul') & (df['longitude'] > center_lon), 'Setor'] = 'Sudeste'
df.loc[(df['Setor'] == 'Norte') & (df['longitude'] < center_lon), 'Setor'] = 'Noroeste'
df.loc[(df['Setor'] == 'Norte') & (df['longitude'] > center_lon), 'Setor'] = 'Nordeste'

# Criar um dicionário de mapeamento para atribuir uma cor a cada setor
cor_setor = {
    'Central': 'crimson',
    'Sul': 'blue',
    'Sudoeste': 'green',
    'Sudeste': 'yellow',
    'Norte': 'purple',
    'Noroeste': 'orange',
    'Nordeste': 'magenta'
}
st.markdown("""
    <style>
        .block-container {
            min-width: 100%;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
        .element-container iframe {
            min-width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .folium-map {
            min-width: 100%;
        }
    </style>
""", unsafe_allow_html=True)



# Criar uma coluna 'Cor' no DataFrame e atribui a cor correspondente a cada setor
df['Cor'] = df['Setor'].map(cor_setor)

# Criar um mapa centrado nas médias dos valores de latitude e longitude
map = folium.Map(location=[center_lat, center_lon], zoom_start=13)


# Adicionar um marcador ao mapa para cada linha do DataFrame
for _, row in df.iterrows():
    
    qtd_moradores = 'Não Informada' if math.isnan(row['qtd']) else int(row['qtd'])
    
    #HTML ddo popup
   
    html = f"""
            <html>
            <head>
            </head>
            <body>
                <div>
                    <h3>INFORMAÇÕES</h3>
                    <p><b>REGIÃO {row['Setor']}.</b></p>
                    <p><b>NÚMERO APROXIMADO DE MORRADORES: {qtd_moradores}</b></p>
                </div>
            </body>
            </html>
            """
    # Cria um iframe com o objeto HTML
    iframe = IFrame(html, width=300, height=150)

    info_pop_up = folium.Popup(iframe, max_width=300)
    folium.Circle(
        location=[row['latitude'], row['longitude']],
        radius=30,
        popup=info_pop_up,
        # Usar a coluna 'Cor' como cor dos círculos
        color=row['Cor'],
        fill=True,
        # Usar a mesma cor para o preenchimento dos círculos
        fill_color=row['Cor'],
        fill_opacity=0.5
    ).add_to(map)





# Contar o número de pontos em cada setor
contagem_setores = df['Setor'].value_counts()

# Renomear a coluna 'index' para 'Setor' e criar uma nova coluna 'Contagem' com os valores da contagem dos setores
contagem_setores = contagem_setores.rename_axis('Setor').reset_index(name='Contagem')

# Criar um objeto de gráfico com os dados da contagem dos setores
chart = alt.Chart(contagem_setores).mark_bar().encode(
    # Usar a coluna 'Setor' como eixo x e dar o nome de 'Setor'
    x=alt.X('Setor', title='Setor'),
    # Usar a coluna 'Contagem' como eixo y e dar o nome de 'Quantidade de Pessoas'
    y=alt.Y('Contagem', title='Quantidade de Pessoas'),
    # Usar a coluna 'Setor' como cor e dar o nome de 'Região'
    color=alt.Color('Setor', title='Região', scale=alt.Scale(
        # Definir as cores dos setores de acordo com as cores dos pontos do mapa
        domain=['Central', 'Sul', 'Sudoeste', 'Sudeste', 'Norte', 'Noroeste', 'Nordeste'],
        range=['crimson', 'blue', 'green', 'yellow', 'purple', 'orange', 'magenta']
    )),
    # Adicionar uma dica de ferramenta com as informações de cada barra
    tooltip=['Setor', 'Contagem']
)


# Display do mapa
sf.folium_static(map)

# Exibir o gráfico usando o st.altair_chart
st.altair_chart(chart,  use_container_width=True)

#   Nesse ponto e importânte resaltar que podem ser utilizados outros tipos de analises estatíosticas
#enciam da base de dados. Com o objetivo de gerar mais informações.