import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import pandas as pd
from read_json import df

#Para descrever o conteúdo de um DataFrame no Pandas

df_info = df.info() # resulta na descrição de cada coluna e seu tipo, com a contagem de valores não nulos,
print(df_info) 

print("------------------------------------")

df_describe = df.describe() # é menos detalhista do que o info(),
print(df_describe) 