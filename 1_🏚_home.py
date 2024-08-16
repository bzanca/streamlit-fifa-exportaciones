import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path

pasta_atual = Path(__file__).parents[0]
caminho_arquivo = Path(pasta_atual/"datasets/CLEAN_FIFA23_official_data.csv")
if "data" not in st.session_state: 
    df_data = pd.read_csv(caminho_arquivo, index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"]>0]
    df_data = df_data.sort_values(by="Overall", ascending = False)
    st.session_state["data"] = df_data


st.markdown('#  FIFA23 OFFICIAL DATASET! ⚽')
st.sidebar.markdown("Desenvolvido por [Exportaciones Zancanaro]")
st.markdown(

"""CONTEXTO

O Conjunto de Dados de Jogadores de Futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de futebol profissionais. 
O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos dos jogadores, características físicas, estatísticas de jogo, detalhes de contrato e afiliações a clubes. 
**Com mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para analistas de futebol, pesquisadores e entusiastas interessados em explorar vários aspectos do mundo do futebol, 
permitindo o estudo de atributos dos jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento de jogadores ao longo do tempo."""
)

btn = st.link_button("Acesse os dados no Kaggle", "https://kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

