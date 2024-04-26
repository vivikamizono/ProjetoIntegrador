import re
import streamlit as st;
from os import write


st.title("Ogawa Eletrotécnica")

def aceitar_apenas_numeros(entrada):
    return ''.join(filter(str.isdigit, entrada))

with st.form(key="include_cliente"):
    input_name = st.text_input(label="insira seu nome: ")
    
    input_senha = st.text_input(label="Insira sua senha ")
    
    input_button_submit = st.form_submit_button("enviar")
    
## if input_button_submit:
##    st.write(f'Nome: {input_name}')
##    st.write(f'Senha: {input_senha}')
    