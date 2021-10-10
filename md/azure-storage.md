# Taller CLI Azure DataLake Gen 2

## Versiones
`$ az --version`  

## 1) Autenticación
`$ az login` 
* Hacia otro proyecto   
`$ az login --tenant yourdir.onmicrosoft.com`  
* Hacia un suscripción en particular  
`$ az account set --subscription abcdefg-123456789`  

# 2) Crear, subir y mover elementos a containers
### 2.1) Crear container
`$ az storage fs create -n {fs_name} --account-name {storageacc} --auth-mode login`

### 2.2) Subir elemento a container
`$ az storage fs file upload -s mock_data.csv -p mock_data.csv -f {fs_name} --account-name {storageacc} --auth-mode login`

### 2.3) Subir elementos en bloque
#### 2.3.1) Root directory
`$ az storage fs directory upload -f {fs_name} --account-name {storageacc} -s "dummy-data" -r --auth-mode login`

#### 2.3.2) Otro directorio
* Crear directorio  
`$ az storage fs directory create -n directorio -f {fs_name} --account-name {storageacc} --auth-mode login`
* Subir file a directorio  
`$ az storage fs directory upload -f {fs_name} --account-name {storageacc} -s "mock_data.csv" -d directorio -r --auth-mode login`
* Subir múltiples archivos a otro directorio  
`$ az storage fs directory create -n newfolder -f {fs_name} --account-name {storageacc} --auth-mode login`  
`$ az storage fs directory upload -f {fs_name} --account-name {storageacc} -s "dummy-data" -d newfolder -r --auth-mode login`

### 2.4) Mover elementos a nuevo directorio
`$ az storage fs file move --new-path {fs_name}/directorio/mock_data.csv -p mock_data.csv -f {fs_name} --account-name {storageacc} --auth-mode login`  

### 2.5) Mover directorio
`$ az storage fs directory move --new-directory {fs_name}/directorio/newfolder -n newfolder -f {fs_name} --account-name {storageacc} --auth-mode login`  

## 3) Detalles de elementos en storage account
### 3.1) Mostrar containers
`$ az storage fs list --account-name {storageacc} --auth-mode login`  

### 3.2) Mostrar detalles de objetos dentro de container
`$ az storage fs file show -p directorio/newfolder/dummy-data/sql_sales.sql -f {fs_name} --account-name {storageacc} --auth-mode login`  

## 4) Eliminar elementos
### 4.1) Borrar objeto
`$ az storage fs file delete -p directorio/mock_data.csv -f {fs_name} --account-name {storageacc} --yes --auth-mode login`  

### 4.2) Borrar directorio
`$ az storage fs directory delete -n directorio -f {fs_name} --account-name {storageacc} --yes --account-key {acc_key}`  

### 4.3) Eliminar container
`$ az storage fs delete -n {fs_name} --account-name {storageacc} --yes --auth-mode login`  

## 5) Descargar elementos de container
### 5.1) Descargar elemento único
`$ az storage fs file download -p mock_data.csv -d {local_path}/mock_data.csv -f {fs_name} --account-name {storageacc} --account-key {acc_key}`  

### 5.2) Descargar directorio
`$ az storage fs directory download -f {fs_name} --account-name {storageacc} -s "dummy-data" -d {local_path} -r --account-key {acc_key}`  

### 5.3) Descargar todo un container
`$ az storage fs directory download -f {fs_name} --account-name {storageacc} -d {local_path} -r --account-key {acc_key}`  
