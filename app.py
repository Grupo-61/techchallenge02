from pathlib import Path
import pandas as pd
from datetime import datetime
from scrap import obtemDadosB3
import boto3
import os
from dotenv import load_dotenv

_= load_dotenv()

session = boto3.Session(
    aws_access_key_id= os.getenv('aws_access_key_id'),
    aws_secret_access_key= os.getenv('aws_secret_access_key'),
    aws_session_token= os.getenv('aws_session_token'), 
    region_name= os.getenv('region_name')
)

s3 = session.client('s3')

# listar buckets
# response = s3.list_buckets()
# for bucket in response['Buckets']:
#     print(bucket['Name'])

# obtenho dados b3
dados, colunas= obtemDadosB3()
df = pd.DataFrame(dados, columns=colunas)

# crio sub-dir data
subdir= str(datetime.now()).split(" ")[0] 

# exporto .parquet
# destino= "dados/" + subdir
destino= subdir
Path(destino).mkdir(parents=True, exist_ok=True)

#Salvo em .parquet
destino= f'{destino}/dados.parquet'
df.to_parquet(destino, engine='pyarrow', index=False)

# testo scrap
arquivo= Path(destino)

print(f'Arquivo: {arquivo}')

if arquivo.exists():

    # bucket destino
    bucket_name= os.getenv('s3_bucket_destino')
    s3_key= destino
    arquivo_local= arquivo

    # Fazer o upload
    s3.upload_file(arquivo_local, bucket_name, s3_key)
    print("Upload realizado com sucesso!")

else:
    print("Arquivo não encontrado!")


