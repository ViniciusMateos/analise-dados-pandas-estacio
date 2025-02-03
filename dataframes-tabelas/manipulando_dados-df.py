#Quando fazemos uma projeção ou uma seleção, o que queremos é criar um subconjunto dos dados originais
# Tal operação é realizada na linguagem SQL pelo comando SELECT
#enquanto para os DataFrames podemos fazer o mesmo com os métodos loc, iloc e query.

import pandas as pd


df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],

index=['cobra', 'viper', 'sidewinder'],
columns=['max_speed', 'shield'])

print(df.loc['viper']) # A primeira com apenas uma coluna.
print()
print(df.loc[['viper', 'sidewinder']]) # A segunda com duas colunas.

# podemos reparar que, ao selecionarmos apenas uma coluna, teremos de volta uma série (Pandas series
# caso escolhamos mais de uma coluna, além de termos que passar o conjunto como uma lista dentro dos colchetes do loc, o retorno será um DataFrame, uma vez que é o coletivo de duas ou mais séries.

print()

mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
df = pd.DataFrame(mydict)
 
print(df.iloc[0]) # primeira coluna do conjunto.
print()
print(df.iloc[[0]]) # primeira linha do DataFrame.
print()
print(df.iloc[[0, 1]]) # primeira e segunda linhas do DataFrame.
print()
print(df.iloc[:3]) # primeiras linhas do DataFrame.
print()
print(df.iloc[lambda x: x.index % 2 == 0]) # projeção com a condição de que o valor das células seja par.
print()

# projetam uma submatriz (ou filtro) do DataFrame original, o primeiro sendo feito de forma direta e o segundo por fatiamento.
print(df.iloc[[0, 2], [1, 3]])
print()
print(df.iloc[1:3, 0:3])

# exemplo com query
print()


df = pd.DataFrame({'A': range(1, 6),
                    'B': range(10, 0, -2),
                    'C': range(10, 5, -1)})

print(df.query('A > B')) # retorna dados cujo valor da dimensão A é maior do que o da dimensão de B
print()
print(df.query('B == C')) # uma igualdade, em que desejamos os dados cujo valor da dimensão B seja igual ao da dimensão 'C C
                                # repare que, dentro da query, o que for textual, seja valor ou dimensão, tem de ser declarado com o acento crase (`)

print()
print(df[df.A > df.B]) # passando a referência da coluna no colchete do DataFrame.


