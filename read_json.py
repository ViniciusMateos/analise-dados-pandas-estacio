# A função de leitura do Pandas é tão poderosa que pode ler arquivos não convencionais como lista de dicionários, bastando utilizar o método read_json,
# por exemplo, que tem um atributo específico chamado orient, que vem de orientação, uma vez que a lista de dicionários pode ser passada como record, ou seja, por vetor de registros, ou, ao contrário, split, que é vetor de valores de coluna variável.


import pandas as pd
df = pd.read_json('./DIRETÓRIO_DE_DADOS/ARQUIVO.json', orient='records')