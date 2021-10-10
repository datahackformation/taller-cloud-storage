
print('GCP')

# requirements
from google.cloud import storage
import pandas as pd

# common
import os
import pathlib

# Variables
NEW_BUCKET_NAME = 'yourbucketname'
DH_BUCKET = 'taller-storage-gcp'


# 1) OS VARIABLES (Auth)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../secrets/apikey-gcp.json'

# 2) CREAR BUCKET Y SUBIR ELEMENTOS
# 2.1) Crear bucket
storage_client = storage.Client()
bucket = storage_client.create_bucket(
    bucket_or_name=NEW_BUCKET_NAME,
    location='us-east1'
)

# 2.2) Subir elemento a bucket
elem_path = '../data/mock_data.csv'
new_blob = bucket.blob('mock_data.csv')

with open(elem_path, 'rb') as file:
    new_blob.upload_from_file(file)

# 2.3) Subir varios elementos
for e in os.listdir(y := '../data/dummy-data/'):
    with open(y+e, 'rb') as file:
        bucket.blob(f'dummy-data/{e}').upload_from_file(file)

for e in os.listdir(y := '../data/dummy-data/'):
    bucket.blob(f'dummy-data/{e}').upload_from_filename(y+e)

# Multiprocessing example
import multiprocessing as mp
mp.Pool(mp.cpu_count()-2)

# 2.4) Copiar elementos a nuevo folder del bucket
for elem in bucket.list_blobs():
    bucket.copy_blob(
        elem, 
        destination_bucket=bucket,
        new_name=f'copies/{elem.name}'
    )

# 2.5) PANDAS Y GCS
df = pd.read_csv('gs://bucket-ds-py/mock_data.csv')
df.head()
df.groupby('gender')['id'].count().to_csv('gs://bucket-ds-py/mock_data_transformed.csv')

pd.read_csv('../data/mock_data.csv').to_csv('gs://bucket-ds-py/mock_data_pd.csv')
del df

# 3) DETALLES DEL BUCKET
# 3.1) Mostrar elementos del bucket
for elem in bucket.list_blobs():
    print(elem.name)

# 3.2) Mostrar detalles de objetos
for elem in bucket.list_blobs():
    print(elem.name, '---', elem.size, '---', elem.storage_class)

# 4) ELIMINAR ELEMENTOS
# 4.1) Borrar objeto
bucket.blob('mock_data.csv').delete()
bucket.delete_blob('mock_data_pd.csv')

# 4.2) Borrar folder
del_blobs = [x.name for x in bucket.list_blobs() if x.name.startswith('copies/')]
bucket.delete_blobs(del_blobs)

# 4.3) Borrar bucket
bucket.delete(force=True)
del bucket

# 5) DESCARGAR ELEMENTOS DESDE BUCKET
dh_bucket = storage.Client().get_bucket(DH_BUCKET)
pathlib.Path('down-data/all').mkdir(parents=True, exist_ok=True)

# 5.1) Descargar elemento
dh_bucket.blob('mock_data.csv').download_to_filename('down-data/mock_data.csv')

# 5.2) Descargar elementos dentro de folder de bucket
down_list = [x.name for x in dh_bucket.list_blobs() if x.name.startswith('dummy-data/')]
for elem in down_list:
    dh_bucket.blob(elem).download_to_filename('down-data/'+elem.split('/')[1])

# 5.3) Descargar todo un bucket
for elem in dh_bucket.list_blobs():
    dh_bucket.blob(n := elem.name).download_to_filename('down-data/all/'+ n.replace('/', '-'))