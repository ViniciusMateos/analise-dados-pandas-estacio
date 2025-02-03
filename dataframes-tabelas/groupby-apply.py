# agregações em DataFrames
# operações mais utilizadas para a análise dos dados, bem como para a extração de estatísticas básicas, possibilitando uma compreensão holística do conjunto de dados
# Ao agregar dados, estamos reduzindo o conjunto e resumindo-o a métricas, estatísticas e agrupamentos.

# Para agruparmos, é simples. Basta chamarmos o método groupby a partir do DataFrame a ser analisado.

import pandas as pd

df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                            'Parrot', 'Parrot'],
                'Max Speed': [380., 370., 24., 26.]})
grouped = df.groupby(['Animal'])
# aceita uma lista de colunas, que serão os agrupadores, mas só chamar o método de groupby não fará as agregações desejadas. 

print(grouped.mean()) # para fazer a agregações é chamar o método direto, como no exemplo mean(), que calcula a média de todas as colunas numéricas agrupadas pelo tipo de animal.
print()


# Podemos fazer mais de uma agregação ao mesmo tempo,
# passar o método agg(['mean']), que recebe uma lista de agregações cobertas na documentação do método no Pandas.


# Uma coisa interessante, que não acontece nos bancos de dados tradicionais, 
# o index das agregações passa a ser o agrupamento
# Para que isso não ocorra, basta usar o reset_index() no resultado da agregação, com drop=False ou não declarado, para que os indexes não sejam deletados e você perca colunas no DataFrame da agregação.


# operação apply, que é um método do DataFrame e das series, nada mais é do que o equivalente à função map de outras linguagens como Java e Javascript,
# definimos uma função e a passamos nos componentes de uma lista a fim de modificá-la.

# Nos DataFrames, isso pode ser feito pelas colunas individualmente ou pelas linhas, bastando mudar o atributo axis na chamada.

import numpy as np

df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B']) # três linhas, com cada linha tendo os valores 4 e 9.
print(df.apply(np.sqrt)) # queremos a raiz quadrada do DataFrame inteiro, mas apenas para visualização
print()
df['A'] = df['A'].apply(lambda x: x + 1) # modificando a coluna A para que seja acrescida de uma unidade
df['C'] = df.apply(lambda x: x['A']+x['B'], axis=1) # criamos uma nova coluna para ser a soma das colunas A e B.

print(df)