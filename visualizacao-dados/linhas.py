# dados temporais, aqueles que passam ideia de cronologia
# Uma solução natural é representarmos tais dados a partir do gráfico de linhas

import plotly.express as px
df = px.data.gapminder().query("continent=='Oceania'")
fig = px.line(df, x='year', y='lifeExp', color='country')
fig.show()

# Expectativa de vida ao longo dos anos para Austrália e Nova Zelândia (data.gapminder)

# podemos perceber bem a ideia de cronologia, com o eixo X apresentando o dado temporal (anos, meses, datas completas, horas ou mesmo o index do DataFrame).
# Assim, será possível entender a evolução da coluna analisada
# podemos ver, foi feita uma coloração diferente por país, um dado categórico, isto é, uma agregação/agrupamento