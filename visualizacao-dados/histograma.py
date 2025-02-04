import plotly.express as px

# plotly.express, uma API para criação de gráficos no Python que contém diversos datasets de testes, identificados por data.xxx().

df = px.data.tips()
fig = px.histogram(df, x='total_bill')
fig.show()

# Histograma da distribuição de dados de comandas de restaurante (data.tips