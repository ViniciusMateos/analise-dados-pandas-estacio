#Para fins de estudo e demonstração, vamos tratar como se nossos dados recuperados fossem arquivos, como os separados por vírgula, CSV. 

import pandas as pd # importando a biblioteca
df = pd.read_csv('./DIRETÓRIO_DE_DADOS/ARQUIVO.csv') 

#Pandas lê o arquivo separado por vírgulas convertendo-o em estrutura tabelar e, por padrão, a primeira linha do arquivo é considerada o cabeçalho da tabela
# para esse tipo de operação, o leitor de arquivo do Pandas considera a vírgula como separador de colunas e o parágrafo como separador de registros ou linhas.

# Esse padrão pode ser alterado passando o marcador desejado para o parâmetro sep.

# Existe o leitor de Excel (read_excel), que funciona exatamente da mesma forma, com o cabeçalho também na primeira linha por padrão, mas o separador padrão é o tab (espaço tabular
# maior diferença é que no Excel, diferentemente do CSV, pode haver abas (sheets); por padrão, considera-se a primeira aba na leitura.





