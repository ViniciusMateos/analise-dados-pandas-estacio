import pandas as pd

dict=[{'a': 1, 'b': 2, 'c': 3, 'd': 4},
    {'a': 100, 'b': 200, 'c': 300, 'd': 400},
    {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]

df = pd.DataFrame(dict)
print(df)
print()

df.drop(columns=['a'],inplace=True) # ou reassinando sem o inplace

print(df)
print()

# podemos deletar a célula e para isso basta associar o valor None à célula localizada com a ajuda do iloc, ou qualquer outra forma de projeção

#para deletarmos linhas:


df.drop([0,1], inplace=True) # ou reassinando sem o inplace

print(df)
print()

# utilizamos muito os indexes para nossas manipulações
# Para que possamos regularizar a indexação depois de um drop, ou seja, reindexar, basta fazer:

df.reset_index(drop=True, inplace=True) # ou reassinando sem o inplace

print(df)
print()

# Assim como nos bancos de dados, temos também as operações de junção, feitas pelo concat, merge e join.


#CONCAT

s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
s3 = pd.concat([s1, s2], axis=1)
# realiza a junção entre as séries pelos seus indexes
# Basta definir o axis=1, pois normalmente o concat, quando não declarada a axis ou usando axis=0, fará uma união entre os dados. 
# Após um concat, pode ser feito um reset_index também, mas podemos encurtar esse passo declarando dentro do pd.concat() o parâmetro ignore_index=True.

print(s3)
print()


# MERGE

df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                     'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [5, 6, 7, 8]})

print(df1.merge(df2, left_on='lkey', right_on='rkey', suffixes=('_left','_right')))
# declaramos as chaves estrangeiras que serão a base da junção e declaramos os sufixos em caso de repetição de nome de colunas, que é o caso da coluna value, na qual teremos values da esquerda e da direita.
print()


#JOIN

df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
other = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                    'B': ['B0', 'B1', 'B2']})
df = df.join(other, lsuffix='_caller', rsuffix='_other')

print(df)

# join é feito a partir de um dos DataFrames, assim como o merge, mas ele depende do index, e a junção é feita no index padrão.





