# Outro exemplo para entendermos proporções das categorias é o gráfico de pizza ou torta (pie).

import plotly.express as px
df = px.data.tips()
fig = px.pie(df, values='tip', names='day')
fig.show()

# Gráfico de pizza mostrando a proporção dos valores distintos de dias da semana no conjunto de comandas (data.tips

# podemos tanto ver que o conjunto de dados só tem quatro dias distintos como também suas proporções,
# mostrando que o restaurante/lanchonete do conjunto de dados de comandas tem maior funcionamento nos fins de semana.

# gráfico de pizza é adequado quando temos poucas categorias, pois, se ele tiver muitas fatias a exibir, ou seja, muitos valores únicos, passa a ficar ilegível, sendo preferível migrar para o gráfico de barras.



