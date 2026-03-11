import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard de Análise de Dados")

arquivo = st.file_uploader("Envie um arquivo CSV", type=["csv"])

if arquivo is not None:

    df = pd.read_csv(arquivo, encoding="latin1")

    st.subheader("Prévia dos dados")
    st.write(df.head())

    st.subheader("Informações do dataset")
    st.write(df.describe())

    coluna = st.selectbox("Escolha uma coluna", df.columns)

    fig, ax = plt.subplots()
    df[coluna].hist(ax=ax)

    st.pyplot(fig)
