from fastapi import APIRouter, HTTPException
from model.usuario import Usuario as usr

router = APIRouter()

#Iniciar el servidor: uvicorn archivo:route --reload
#Detener el servidor: CTRL + C

user_list = [usr(cedula=987, nombres = "Juan", apellidos= "Marín", direccion= "Pradera"),
             usr(cedula=654, nombres = "Elías", apellidos= "López", direccion= "Canta claro"),
             usr(cedula=123, nombres = "María", apellidos= "Garcés", direccion= "Mogambo"),
             usr(cedula=951, nombres = "Ana", apellidos= "Gómez", direccion= "P5")             
             ]

user_list_II = []

# @route.get('/')
# async def root():       
#    return {'Mensaje':'Bienvenidos a esta API de practica'}

@router.get('/users')
async def users():    
   # return {usr(cedula = 98521, nombres = "Juan", apellidos = "PEREZ", direccion="Pradera")}
   if len(user_list) > 0:
      return user_list
   else:
      return {'Mensaje':'lista vacía'}

# Pedir el dato por el path
# Cuando un dato se pide por el path es obligatorio
@router.get('/user/{user_id}')
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
@router.get('/userquery/')
async def user(ced : int):    
   # return {usr(cedula = 98521, nombres = "Juan", apellidos = "PEREZ", direccion="Pradera")}
   #funcion de orde superior
#    resultado = filter(lambda usr: usr.cedula == ced, user_list)
#    try:
#     return list(resultado)[0]
#    except:
#     return {'Mensaje':'No se ha encontrado al usuario'}
    return serch_user(ced)

@router.post('/add_user/',status_code=201, response_model=usr)
async def add_user(param_usr : usr):
   #primero comprobamos si el usuario existe en la lista
   if type(serch_user(param_usr.cedula)) == usr:
      #return {'Error':f'El usuario {param_usr.nombres} con cédula {param_usr.cedula} ya existe en la lista'}
      raise HTTPException(status_code=404, detail=f'El usuario con {param_usr.cedula} con nombre {param_usr.nombres} ya existe en la lista')
   else:
      user_list.append(param_usr)
      return param_usr
       
@router.put('/update_user/')
async def update_user(param_usr :usr):
   estado = False
   
   for index, dato in enumerate(user_list):
      if dato.cedula == param_usr.cedula:
         user_list[index] = param_usr
         estado = True
         #return{'Mensaje' : f'Usuario {dato.nombres} actualizado correctamente!'}
         return param_usr
   
   if estado == False:
      return {'Error': f'No se ha encontrado al usuario con cédula {param_usr.cedula}'}


# Cuando se crea un parametro por el path dentro del método se debe llamar igual 
@router.delete('/delete_user/{cedula}')
async def delete_user(cedula : int):
   for dato in user_list:
      if dato.cedula == cedula:
         user_list.remove(dato)   
         return {'Resultado' : 'Usuario eliminado'}
      else:
         return {'Resultado' : 'No existe el usuario'}

# Tambien se pueden crear métodos que se usen en diferentes peticiones
# Creamos un método
def serch_user(ced: int):
    #funcion de orde superior
   resultado = filter(lambda usr: usr.cedula == ced, user_list)
   try:
    return list(resultado)[0]
   except:
    return {'Mensaje':'No se ha encontrado al usuario'}