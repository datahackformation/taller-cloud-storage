
print('Azure')

# requirements
from azure.storage.filedatalake import DataLakeServiceClient
import os

# 1) AUTH
STORAGE_ACCOUNT = 'tallerstorageazure'
URL_STRING = 'https://{}.dfs.core.windows.net'.format(STORAGE_ACCOUNT)

with open('../secrets/apikey-azure.txt', 'r') as key:
    STORAGE_ACC_KEY = key.read()

# 2) OPERACIONES CON CONTAINERS
# 2.1) Crear container
az_client = DataLakeServiceClient(account_url=URL_STRING, credential=STORAGE_ACC_KEY)
file_system_client = az_client.create_file_system(file_system='container-ds-py')

# 2.2) Crear directorio
file_system_client.create_directory('nuevo-dir')

# 2.3) Subir elemento a container
local_file_path = '../data/mock_data.csv'
local_video_path = '../data/test.mp4'

file_system_client.create_file('mock_data.csv')
file_system_client.create_file('test.mp4')

file_client = file_system_client.get_file_client('mock_data.csv')
file_client_video = file_system_client.get_file_client('test.mp4')

with open(local_file_path, 'rb') as file:
    file_client.upload_data(file, overwrite=True)

with open(local_video_path, 'rb') as file:
    file_client_video.upload_data(file, overwrite=True)

# 2.4) Subir múltiples elementos a directorio
data_path = '../data/dummy-data/'
file_names = os.listdir(data_path)

for f in file_names:
    f_client = file_system_client.create_file(f'dummy-data/{f}')
    with open(f'{data_path + f}', 'rb') as uf:
        f_client.upload_data(uf, overwrite=True)

# 2.5) Mover elementos a directorio
path_dir = 'container-ds-py/nuevo-dir/mock_data.csv'
file_client.rename_file(path_dir)

# 2.6) Mover directorio completo
dir_client = file_system_client.get_directory_client('nuevo-dir')
dir_client.rename_directory('container-ds-py/dummy-data/nuevo-dir')

# 3) DETALLES DE ELEMENTOS EN STORAGE ACCOUNT
# 3.1) Mostrar containers
for x in az_client.list_file_systems():
    print(x.name)

# 3.2) Mostrar detalles de elementos dentro de container
for x in file_system_client.get_paths():
    print(x.name)

# 4) ELIMINAR ELEMENTOS
# 4.1) Borrar elemento
file_system_client.delete_file('test.mp4')

# 4.2) Borrar directorio completo
file_system_client.delete_directory('dummy-data/nuevo-dir')

# 4.3) Eliminar container
file_system_client.delete_file_system()

# Close client
file_system_client.close()

# 5) Descargar elementos de container
df_fs_client = az_client.get_file_system_client('taller-storage-azure')
local_az_down = '../data/download-storage/taller-azure/'

# 5.1) Descargar elemento único
file_client = df_fs_client.get_file_client('mock_data.csv')
file_client_json = df_fs_client.get_file_client('dummy-data/json_sales.json')

with open(local_az_down + 'mock_data.csv', 'wb') as sfile:
    downloader = file_client.download_file()
    downloader.readinto(sfile)

with open(local_az_down + 'json_sales.json', 'wb') as sfile:
    downloader = file_client_json.download_file()
    downloader.readinto(sfile)

# 5.2) Descargar directorio
local_path = local_az_down + 'multiple/'

for x in df_fs_client.get_paths(path='dummy-data'):
    with open(local_path + x.name.lstrip('dummy-data/'), 'wb') as sflocal:
        downloader = df_fs_client.get_file_client(x.name).download_file()
        downloader.readinto(sflocal)

# 5.3) Descargar todo un container
all_path = local_az_down + 'all/'
valid_paths = [x.name for x in df_fs_client.get_paths() if '.' in x.name]

for az_fname in valid_paths:
    with open(all_path + az_fname.split('/')[-1], 'wb') as sflocal:
        downloader = df_fs_client.get_file_client(az_fname).download_file()
        downloader.readinto(sflocal)