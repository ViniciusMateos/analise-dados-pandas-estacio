# Para dados categóricos, queremos mostrar as categorias e suas proporções

import plotly.express as px
long_df = px.data.medals_long()
fig = px.bar(long_df, x='nation', y='count', color='medal', title='Long-Form Input')
fig.show()
# Exemplo de quadro hipotético de medalhas da China, Coreia do Sul e Canadá em um gráfico de barras