# conversão de dados mais comum é transformar listas de dicionários em DataFrames

import pandas as pd
json_array=[ {'a':1,'b':2}, {'a':3,'b':4}, {'a':5,'b':6} ] 
df = pd.DataFrame(json_array)
print(df)