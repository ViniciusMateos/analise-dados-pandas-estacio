#Assim como é possível ler os arquivos, também é possível persistirmos com eles;
# método usado para isso é to_csv, to_excel, to_json etc
# Deve-se dar especial atenção à persistência, pois em casos como a exportação dos dados no formato de lista de dicionários, ou JSON Array, o padrão de orientação é importantíssimo porque interfere na retrocompatibilidade com outros sistemas que compartilhem os dados.

import pandas as pd
json_array=[ {'a':1,'b':2}, {'a':3,'b':4}, {'a':5,'b':6} ] 
df = pd.DataFrame(json_array)
df.to_json('DIRETÓRIO_DE_DADOS\ARQUIVO.json', orient='records')

# Existem formas ainda mais extravagantes de se ler dados com o Pandas como o read_sql, que lê os dados a partir de conexões ODBC ou JDBC com bancos de dados compatíveis, sendo que cada tipo de banco tem suas especificidades
# Ainda há a possibilidade de leitura por URL, em que, no lugar de passarmos o caminho de diretórios local da máquina, passamos o caminho do arquivo no sistema on-line, que será transferido para o projeto Python seguindo um protocolo FTP.


