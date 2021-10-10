# Taller CLI Google Cloud Storage

## Versiones
`$ gcloud --version`  
`$ gsutil --version`  
`$ bq version`  

## 1) Autenticación
`$ gcloud init`  

## 2) Crear, subir y copiar elementos a buckets
### 2.1) Crear bucket con location (flag `-l`)
`$ gsutil mb -l us-east1 gs://{bucket_name}`  

### 2.2) Subir elemento
`$ gsutil cp mock_data.csv gs://{bucket_name}`  
`$ gsutil cp test.mp4 gs://{bucket_name}`  

### 2.3) Subir elementos en bloque
#### 2.3.1) Flag `-r`
`$ gsutil cp -r dummy-data gs://{bucket_name}`  

#### 2.3.2) Flag `-m`
`$ gsutil -m cp -r dummy-data gs://{bucket_name}/mp`  

### 2.4) Copiar elementos a nuevo folder
`$ gsutil cp gs://{bucket_name}/mock_data.csv gs://{bucket_name}/dummy-data/mock_data.csv`  

## 3) Detalles de elementos en buckets
### 3.1) Mostrar elementos del bucket
`$ gsutil ls gs://{bucket_name}`  
`$ gsutil ls -r gs://{bucket_name}`  

### 3.2) Mostrar detalles de objetos
`$ gsutil ls -l gs://{bucket_name}/mock_data.csv`  
`$ gsutil ls -l gs://{bucket_name}/dummy-data`  

## 4) Eliminar elementos
### 4.1) Borrar objeto
`$ gsutil rm gs://{bucket_name}/mock_data.csv`  

### 4.2) Borrar folder
`$ gsutil rm -r gs://{bucket_name}/dummy-data`  

### 4.3) Eliminar bucket
`$ gsutil rm -r gs://{bucket_name}`  

## 5) Descargar elementos de bucket
### 5.1) Descargar elemento único
`$ gsutil cp gs://{bucket_name}/mock_data.csv {local_path}/mock_data.csv`  

### 5.2) Descargar elementos dentro de folder de bucket
`$ gsutil cp gs://{bucket_name}/dummy-data/json_sales.json {local_path}/json_sales.json`  
`$ gsutil -m cp -r gs://{bucket_name}/dummy-data {local_path}`  

### 5.3) Descargar todo un bucket
`$ gsutil -m cp -r gs://{bucket_name} {local_path}`  