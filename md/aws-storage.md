# Taller CLI AWS S3

## Versiones
`$ aws --version`  

## 1) Autenticación
`$ aws configure`  

## 2) Crear, subir y copiar elementos a buckets
### 2.1) Crear bucket con location
`$ aws s3 mb s3://{bucket_name} --region us-west-1`  

### 2.2) Subir elemento
`$ aws s3 cp mock_data.csv s3://{bucket_name}`  
`$ aws s3 cp test.mp4 s3://{bucket_name}`  

### 2.3) Subir elementos en bloque
`$ aws s3 cp dummy-data s3://{bucket_name}/dummy-data --recursive`  
`$ aws s3 cp . s3://{bucket_name}/all --recursive`  

### 2.4) Mover o copiar elementos a nuevo folder
`$ aws s3 mv s3://{bucket_name}/test.mp4 s3://{bucket_name}/dummy-data/test.mp4`  
`$ aws s3 cp s3://{bucket_name}/mock_data.csv s3://{bucket_name}/dummy-data/mock_data.csv`  

## 3) Detalles de elementos en buckets
### 3.1) Mostrar buckets
`$ aws s3 ls`  

### 3.2) Mostrar elementos y detalles dentro de bucket
`$ aws s3 ls s3://{bucket_name}`  
`$ aws s3 ls s3://{bucket_name} --recursive --summarize`  

## 4) Eliminar elementos
### 4.1) Borrar objeto
`$ aws s3 rm s3://{bucket_name}/mock_data.csv`  

### 4.2) Borrar folder
`$ aws s3 rm s3://{bucket_name}/all --recursive`  

### 4.3) Eliminar bucket
`$ aws s3 rb s3://{bucket_name}`  
`$ aws s3 rb s3://{bucket_name} --force`  

## 5) Descargar elementos de bucket
### 5.1) Descargar elemento único
`$ aws s3 cp s3://{bucket_name}/mock_data.csv mock_data.csv`  

### 5.2) Descargar elementos dentro de folder de bucket
`$ aws s3 cp s3://{bucket_name}/dummy-data/json_sales.json {local_path}/json_sales.json`  
`$ aws s3 cp s3://{bucket_name}/dummy-data {local_path}/dummy-data/ --recursive`  

### 5.3) Descargar todo un bucket
`$ aws s3 cp s3://{bucket_name} {local_path}/all/ --recursive`  