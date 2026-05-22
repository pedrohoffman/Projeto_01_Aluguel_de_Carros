import streamlit as st
st.title('motors grid leal')
st.subheader(' nao vendemos carros vendemos experiencias ')
st.sidebar.title('escolha seu broto')
st.sidebar.image('logo.png')
carros=['koinigsegg','ferrari','pagani','porsche','mercedes']
opcao = st.sidebar.selectbox('escolha o carro que foi alugado',carros)


st.image(f"{opcao}.png")
st.markdown(f"## Você alugou o modelo: {opcao}")
st.markdown("---")