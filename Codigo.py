import streamlit as st
import pandas as pd
import plotly.express as px

#carregar base de vendas
df_vendas = pd.read_csv("vendas.csv", sep=";")
df_vendas["data"] = pd.to_datetime(df_vendas["data"], dayfirst=True)

st.write("# Sistema de vendas")

#cadastro de vendas
st.sidebar.write("## Cadastrar vendas")
data = st.sidebar.date_input("Data")
vendedor =st.sidebar.selectbox("Vendedor", ["Raul", "Malu", "Luiz"])
produto = st.sidebar.selectbox("Produto", ["Camiseta", "SSD", "piercing", "Mouse", "Teclado"])
quantidade = st.sidebar.number_input("Quantidade", step=1)   
valor =st.sidebar.number_input("Valor unitário")
botao_cadastrar =st.sidebar.button("Cadastrar venda")

#botao cadastrar
if botao_cadastrar:
    if valor <= 0:
        st.warning("Valor vazio ou inválido")
    else:
         nova_venda = [str(data), vendedor, produto, quantidade, valor]
    print(nova_venda)
    ultima_linha = len(df_vendas)
    df_vendas.loc[ultima_linha] = nova_venda
    df_vendas.to_csv("vendas.csv", sep=";", index=False)
    st.success("Venda Cadastrada")

    
#visualização de vendas
st.write("## Vendas Cadastradas")
st.dataframe(df_vendas)



#visualizaçao dashboard
st.write("## Dashboard")

#faturamento total
faturamento = df_vendas["valor"].sum()
st.metric("Faturamento total", faturamento)

#grafico1
grafico1= px.bar(df_vendas, x="vendedor", y="valor", color="produto", )  
st.plotly_chart(grafico1)

#grafico2
grafico2 = px.pie(df_vendas, names="produto", values="valor", hole = 0.5)
st.plotly_chart(grafico2)
 