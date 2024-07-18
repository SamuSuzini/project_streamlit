import streamlit as st
import pandas as pd
from datetime import date


def gravar_dados(nome, dt_nasc, tipo):
    erros = []
    
    if tipo not in ["Pessoa física", "Pessoa Jurídica"]:
        erros.append("Por favor, selecione um tipo de cliente válido.")
    
    if dt_nasc is None:
        erros.append("Por favor, preencha a data de nascimento.")
    
    if not nome:
        erros.append("Por favor, preencha o nome.")
    
    if dt_nasc is not None and dt_nasc > date.today():
        erros.append("A data de nascimento não pode ser no futuro.")
    
    if erros:
        for erro in erros:
            st.error(erro)
        st.session_state["Sucesso"] = False
    else:
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{dt_nasc},{tipo}\n")
        st.session_state["Sucesso"] = True
        st.success("Dados preenchidos corretamente.")

                
        st.session_state["nome"] = ""
        st.session_state["dt_nasc"] = None
        st.session_state["tipo"] = "Selecione..."




st.set_page_config(
page_title="Cadastro",
page_icon="😎"

)

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente",
                     key="nome_cliente")

dt_nasc = st.date_input("Data de Nascimento",
                        format="DD/MM/YYYY",
                        value=None)

tipo = st.selectbox("Tipo do Cliente",
                     ["-----","Pessoa física", "Pessoa Juridica"],
                )

btn_cadastrar = st.button("Cadastrar",
                          on_click=gravar_dados,
                          args=[nome, dt_nasc, tipo]
                          )

if btn_cadastrar:
    if st.session_state["Sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✅")
    else:
        st.error("Houve algum problema no cadatro!",
                 icon="❌")