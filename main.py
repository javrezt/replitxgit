import streamlit as st

st.title("Github + Streamlit")

query = st.text_input("¿Cuál es tu consulta?")

st.markdown(f"Tu consulta es: {query}")