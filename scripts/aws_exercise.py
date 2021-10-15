
print('AWS')

# requirements
import boto3
import pandas as pd
import s3fs

# common
import os
import json
import pathlib

# variables
NEW_BUCKET_NAME = 'david-bucket-taller'
DH_BUCKET = 'taller-storage-aws'

# 1) OS VARIABLES (Auth)
with open('../secrets/apikey-aws.json') as keyfile:
    keys = json.load(keyfile)

os.environ['AWS_ACCESS_KEY_ID'] = keys['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY'] = keys['AWS_SECRET_ACCESS_KEY']

# 2) CREAR BUCKET Y SUBIR ELEMENTOS
# 2.1) Crear bucket
s3_client = boto3.client('s3')
s3_client.create_bucket(
    Bucket=NEW_BUCKET_NAME, 
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    }
)

# 2.2) Subir elemento a bucket
elem_path = '../data/mock_data.csv'
elem_path_video = '../data/test.mp4'

with open(elem_path, 'rb') as file:
    s3_client.upload_fileobj(file, NEW_BUCKET_NAME, 'mock_data.csv')

s3_client.upload_file(elem_path_video, NEW_BUCKET_NAME, 'test.mp4')

# 2.3) Subir varios elementos
elems = os.listdir(y := '../data/dummy-data/')
for e in elems:
    s3_client.upload_file(y + e, NEW_BUCKET_NAME, f'dummy-data/{e}')

# Multiprocessing example
import multiprocessing as mp
mp.Pool(mp.cpu_count()-2)

# 2.4) Copiar elementos a nuevo folder/bucket
s3_client.copy(
    CopySource={
        'Bucket': NEW_BUCKET_NAME, 
        'Key': 'mock_data.csv'
    }, 
    Bucket=NEW_BUCKET_NAME, 
    Key='dummy-data/mock_data.csv'
)

# 2.3) PANDAS Y S3
file = s3_client.get_object(Bucket=NEW_BUCKET_NAME, Key='mock_data.csv')
df = pd.read_csv(file['Body'])
df.head()

# 3) DETALLES DEL BUCKET
# 3.1) Mostrar buckets
s3_client.list_buckets()['Buckets']

# 3.2) Mostrar elementos en bucket
for elem in s3_client.list_objects_v2(Bucket=NEW_BUCKET_NAME)['Contents']:
    print(elem['Key'])

# 4) ELIMINAR ELEMENTOS
# 4.1) Borrar objeto
s3_client.delete_object(
    Bucket=NEW_BUCKET_NAME,
    Key='test.mp4',
)

# 4.2) Borrar folder
# Multiples elementos
s3_client.delete_objects(
    Bucket=NEW_BUCKET_NAME,
    Delete={
        'Objects': [
            {'Key': 'mock_data.csv'},
            {'Key': 'dummy-data/mock_data.csv'},
            {'Key': 'dummy-data/customcsv_sales.txt'}
        ],
    }
)

# Folder
base_objects = s3_client.list_objects_v2(Bucket=NEW_BUCKET_NAME)['Contents']
elementos = [e.get('Key') for e in base_objects if 'dummy-data/' in e.get('Key')]
objects = [{v: k} for k,v in dict.fromkeys(elementos, 'Key').items()]

s3_client.delete_objects(
    Bucket=NEW_BUCKET_NAME,
    Delete={'Objects': objects}
)

# 4.3) Borrar bucket
s3_client.delete_bucket(Bucket=NEW_BUCKET_NAME)

# 5) DESCARGAR ELEMENTOS DESDE BUCKET
local_path = '../data/download-storage/taller-aws/aws-py-download/'

# 5.1) Descargar elemento
s3_client.download_file(DH_BUCKET, 'mock_data.csv', local_path+'mock_data.csv')

with open(local_path+'json_sales.json', 'wb') as file:
    s3_client.download_fileobj(DH_BUCKET, 'dummy-data/json_sales.json', file)

# 5.2) Descargar elementos dentro de folder de bucket
pathlib.Path(local_path+'dummy-data').mkdir(parents=True, exist_ok=True)
dummy_data_path = local_path+'dummy-data/'

base_objects = s3_client.list_objects_v2(Bucket=DH_BUCKET)['Contents']
dummy_elems = [e.get('Key') for e in base_objects if 'dummy-data/' in e.get('Key')]

for e in dummy_elems:
    s3_client.download_file(DH_BUCKET, e, dummy_data_path + e.split('/')[-1])

# 5.3) Descargar todo un bucket
pathlib.Path(local_path+DH_BUCKET).mkdir(parents=True, exist_ok=True)
taller_all_path = local_path+ '%s/'%DH_BUCKET

dh_base_objects = s3_client.list_objects_v2(Bucket=DH_BUCKET)['Contents']
dh_elementos = [e.get('Key') for e in base_objects]

for e in dh_elementos:
    s3_client.download_file(DH_BUCKET, e, taller_all_path + e.split('/')[-1])
