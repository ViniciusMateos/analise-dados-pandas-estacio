# podemos querer saber a correlação entre dados numéricos e, para isso, podemos utilizar o gráfico de dispersão, scatterplot

import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', symbol='species')
fig.show()

# Gráfico de dispersão de larguras e comprimentos de sépala de flores (data.iris) 
# No gráfico, podemos ver a relação entre as medidas, agregadas pela espécie.
