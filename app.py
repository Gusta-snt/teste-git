import streamlit as st
from pages import tela_analise, tela_inicial

st.set_page_config(page_title="Análise de Dados Iris", page_icon="🌸")

if "tela" not in st.session_state:
    st.session_state["tela"] = "inicial"

if st.session_state["tela"] == "inicial":
    tela_inicial()
else:
    tela_analise()
