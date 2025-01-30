#Vale ressaltar que nem todos os arquivos JSON já vêm no formato de lista de dicionários, mas sim como strings convertidas
# é considerada uma boa prática tentar fazer a decodificação caso haja a dúvida:

import pandas as pd
import json
json_array='[ {"a":1,"b":2}, {"a":3,"b":4}, {"a":5,"b":6} ]'
df = pd.DataFrame(json.loads(json_array) )
print(df)