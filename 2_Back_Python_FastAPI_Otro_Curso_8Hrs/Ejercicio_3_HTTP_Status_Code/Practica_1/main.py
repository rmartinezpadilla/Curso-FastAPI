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
        #return {'Telefonos' : list_phone}
        return list_phone


# ----------------- IMPORTANTE -----------------
#     Agregamos dentro del  metodo add_phone el parametro response_model= '' 
#     para decirle al método en caso de que todo vaya bien responda dicho objeto
#     podemos decirle al metodo que va a recibir si todo va bien y que va a devolver 
    
@app.post('/phone/',status_code=201, response_model=phone)
async def add_phone(cel : phone):
     #primero comprobamos si el telefono existe en la lista
   if type(serch_phone(cel.id)) == phone:
       # Creamos una respuesta al error de respues 204
       # return HTTPException(status_code=204, detail=f'El telfono {cel.marca} con id {cel.id} ya existe en la lista')
       #controlamos el mensaje de error de la respuesta
       raise HTTPException(status_code=404, detail=f'El telefono {cel.marca} con id {cel.id} ya existe en la lista')
      #return {'Error':f'El telfono {cel.marca} con id {cel.id} ya existe en la lista'}
   else:
      list_phone.append(cel)
      return cel
      

#tambien se pueden crear métodos que se usen en diferentes petidiciones
#creamos un método
def serch_phone(id : int):
    #funcion de orde superior
   resultado = filter(lambda phone: phone.id == id, list_phone)
   try:
    return list(resultado)[0]
   except:
    return {'Mensaje':'No se ha encontrado al usuario'}