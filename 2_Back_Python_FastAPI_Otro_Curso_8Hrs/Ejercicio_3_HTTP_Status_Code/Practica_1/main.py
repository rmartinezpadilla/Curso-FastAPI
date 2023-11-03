from fastapi import FastAPI
#importamos la clase celular
from model.celular import Celular as phone



# Instanciamos la clase FastAPI
app = FastAPI()

#Creamos una lista para almacenar los telefonos
list_phone = []

@app.get('/')
async def root():
    return {'Mensaje' : 'Bienvenido'}

@app.post('/phone')
async def add_phone(cel : phone):
    list_phone.append(cel)
    return[cel]