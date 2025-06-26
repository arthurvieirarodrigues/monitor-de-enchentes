# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scripts.previsao_api import get_previsao_15_dias

# Carregar dados históricos
df_1941 = pd.read_csv('data/chuva_1941.csv')
df_2024 = pd.read_csv('data/chuva_2024.csv')
df_previsao = get_previsao_15_dias()

st.set_page_config(page_title="Risco de Enchente em Porto Alegre", layout="wide")
st.title("Risco de Enchente em Porto Alegre")

st.markdown("### Precipitação em 1941")
fig1, ax1 = plt.subplots()
ax1.plot(df_1941['data'], df_1941['precipitacao'], label='1941', color='blue')
ax1.set_xlabel('Dia/Mês')
ax1.set_ylabel('Precipitação (mm)')
ax1.set_title('Chuvas em 1941')
plt.xticks(rotation=45)
st.pyplot(fig1)

st.markdown("### Precipitação em 2024")
fig2, ax2 = plt.subplots()
ax2.plot(df_2024['data'], df_2024['precipitacao'], label='2024', color='red')
ax2.set_xlabel('Dia/Mês')
ax2.set_ylabel('Precipitação (mm)')
ax2.set_title('Chuvas em 2024')
plt.xticks(rotation=45)
st.pyplot(fig2)

st.markdown("### Precipitação no mês atual")
df_mes_atual = df_2024[df_2024['data'].str.startswith(pd.Timestamp.now().strftime('%Y-%m'))]
fig3, ax3 = plt.subplots()
ax3.bar(df_mes_atual['data'], df_mes_atual['precipitacao'], color='orange')
ax3.set_title('Chuvas em ' + pd.Timestamp.now().strftime('%B de %Y'))
plt.xticks(rotation=45)
st.pyplot(fig3)

st.markdown("### Previsão dos próximos 15 dias")
fig4, ax4 = plt.subplots()
ax4.bar(df_previsao['data'], df_previsao['precipitacao'], color='green')
ax4.set_title('Previsão de Precipitação (15 dias)')
plt.xticks(rotation=45)
st.pyplot(fig4)