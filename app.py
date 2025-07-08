from pathlib import Path
import pandas as pd
from datetime import datetime
from scrap import obtemDadosB3

# obtenho dados b3
dados, colunas= obtemDadosB3()
df = pd.DataFrame(dados, columns=colunas)

# crio sub-dir data
subdir= str(datetime.now()).split(" ")[0] 

# logica boto3 

# exporto .parquet
destino= "dados/" + subdir
Path(destino).mkdir(parents=True, exist_ok=True)

#Salvo em .parquet
df.to_parquet(f'{destino}/dados.parquet', engine='pyarrow', index=False)