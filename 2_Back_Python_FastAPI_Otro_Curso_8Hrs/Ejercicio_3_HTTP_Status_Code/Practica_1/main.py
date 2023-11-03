#importmos fasta aí y HTTPException
from fastapi import FastAPI, HTTPException
#importamos la clase celular
from model.celular import Celular as phone

# Instanciamos la clase FastAPI
app = FastAPI()

#Creamos una lista para almacenar los telefonos
list_phone = []

@app.get('/')
async def root():
    return {'Mensaje' : 'Bienvenido'}

@app.get('/phones/')
async def get_phones():
    #if len(list_phone) == 0:
    if not bool(list_phone):
        return {'Mensaje':'Lista vacía'}
    else:        
        return {'Telefonos' : list_phone}

@app.post('/phone/', status_code=201)
async def add_phone(cel : phone):
     #primero comprobamos si el telefono existe en la lista
   if type(serch_phone(cel.id)) == phone:
      return {'Error':f'El telfono {cel.marca} con id {cel.id} ya existe en la lista'}
   else:
      list_phone.append(cel)
      return {'Mensaje' :  cel}
      

#tambien se pueden crear métodos que se usen en diferentes petidiciones
#creamos un método
def serch_phone(id : int):
    #funcion de orde superior
   resultado = filter(lambda phone: phone.id == id, list_phone)
   try:
    return list(resultado)[0]
   except:
    return {'Mensaje':'No se ha encontrado al usuario'}