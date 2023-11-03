from fastapi import FastAPI
from model.usuario import Usuario as usr

app = FastAPI()

#Iniciar el servidor: uvicorn archivo:app --reload
#Detener el servidor: CTRL + C

user_list = [usr(cedula=987, nombres = "Juan", apellidos= "Marín", direccion= "Pradera"),
             usr(cedula=654, nombres = "Elías", apellidos= "López", direccion= "Canta claro"),
             usr(cedula=123, nombres = "María", apellidos= "Garcés", direccion= "Mogambo"),
             usr(cedula=951, nombres = "Ana", apellidos= "Gómez", direccion= "P5")             
             ]

user_list_II = []

@app.get('/')
async def root():       
   return {'Mensaje':'Bienvenidos a esta API de practica'}

@app.get('/users')
async def users():    
   # return {usr(cedula = 98521, nombres = "Juan", apellidos = "PEREZ", direccion="Pradera")}
   if len(user_list) > 0:
      return user_list
   else:
      return {'Mensaje':'lista vacía'}

# Pedir el dato por el path
# Cuando un dato se pide por el path es obligatorio
@app.get('/user/{user_id}')
async def user(ced : int):    
   # return {usr(cedula = 98521, nombres = "Juan", apellidos = "PEREZ", direccion="Pradera")}
   #funcion de orde superior
#    resultado = filter(lambda usr: usr.cedula == ced, user_list)
#    try:
#     return list(resultado)[0]
#    except:
#     return {'La lista está vacía'}
    return serch_user(ced)

# Pedir el dato por una query    
@app.get('/userquery/')
async def user(ced : int):    
   # return {usr(cedula = 98521, nombres = "Juan", apellidos = "PEREZ", direccion="Pradera")}
   #funcion de orde superior
#    resultado = filter(lambda usr: usr.cedula == ced, user_list)
#    try:
#     return list(resultado)[0]
#    except:
#     return {'Mensaje':'No se ha encontrado al usuario'}
    return serch_user(ced)

@app.post('/add_user/')
async def add_user(param_usr : usr):
   #primero comprobamos si el usuario existe en la lista
   if type(serch_user(param_usr.cedula)) == usr:
      return {'Error':f'El usuario {param_usr.nombres} con cédula {param_usr.cedula} ya existe en la lista'}
   else:
      user_list.append(param_usr)
       
@app.put('/update_user/')
async def update_user(param_usr :usr):
   estado = False
   
   for index, dato in enumerate(user_list):
      if dato.cedula == param_usr.cedula:
         user_list[index] = param_usr
         estado = True
         #return{'Mensaje' : f'Usuario {dato.nombres} actualizado correctamente!'}
         return param_usr
   
   if estado == False:
      return {'Error':f'No se ha encontrado al usuario con cédula {param_usr.cedula}'}

@app.delete('/delete_user/{cedula}')
async def delete_user(ced : int):
   for dato in user_list:
      if dato.cedula == ced:
         user_list.remove(dato)   
         return {'Resultado' : 'Usuario eliminado'}
   else:
      return {'Resultado' : 'No existe el usuario'}

#tambien se pueden crear métodos que se usen en diferentes petidiciones
#creamos un método
def serch_user(ced: int):
    #funcion de orde superior
   resultado = filter(lambda usr: usr.cedula == ced, user_list)
   try:
    return list(resultado)[0]
   except:
    return {'Mensaje':'No se ha encontrado al usuario'}