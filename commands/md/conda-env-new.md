# Comandos Conda y Jupyter

## 1) Create env
`$ conda create --name storagecloud`  

## 2) Acceder a virtual env
`$ conda activate storagecloud`  

## 3) Instalar requirements en virtual env
`$ pip3 install -r requirements.txt`  

## 4) Configurar Jupyter new env (para trabajar en Jupyter Notebook)
`$ python -m ipykernel install --user --name=storagecloud`  

## 5) Remove Jupyter env
`$ jupyter kernelspec uninstall storagecloud`  