# Users DB API
from fastapi import APIRouter, HTTPException, status
from db.models.user import Usuario as usr
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId

# Agregamos el parametro prefix='/users' dentro de la instancia APIRouter para no repetirlo en cada path que se cree
#Ejemplo
"""    router =  APIRouter(prefix='/users')
"""
# Para personalizar cada api dentro de la instancia de APIRouter tambien se agregan los siguientes parametros generales
#Ejemplo
"""
router =  APIRouter(prefix='/users', tags=['Users']} )
"""

# Para generalizar una respuesta de error dentro de la API escribimos
# dentro de la instancia de APIRouter tambien se agregan los siguientes parametros generales
#Ejemplo
"""
router =  APIRouter(responses={404 : {'Mensaje' : 'No encontrado'}})
"""

# ------------------------- IMPORTANTE ---------------------
# Nos queda de la siguiente manera

router = APIRouter(prefix='/usersdb', tags=['UsersDB'], responses={404 : {'mensaje' : 'No encontrado'}})

#Iniciar el servidor: uvicorn archivo:route --reload
#Detener el servidor: CTRL + C

user_list = []

# @route.get('/')
# async def root():       
#    return {'Mensaje':'Bienvenidos a esta API de practica'}

@router.get('/', response_model=list[usr])
async def Allusers():    
   # return {usr(cedula = 98521, nombres = "Juan", apellidos = "PEREZ", direccion="Pradera")}
   users = db_client.Ejercicio.Usuario.find()   
   return users_schema(users)
   # if len(user_list) > 0:
   #    return user_list
   # else:
   #    return {'Mensaje':'lista vacía'}


# Pedir el dato por el path
# Cuando un dato se pide por el path es obligatorio
@router.get('/usercedula/{cedula}')
async def user(cedula : int):    
   # return {usr(cedula = 98521, nombres = "Juan", apellidos = "PEREZ", direccion="Pradera")}
   #funcion de orde superior
#    resultado = filter(lambda usr: usr.cedula == ced, user_list)
#    try:
#     return list(resultado)[0]
#    except:
#     return {'La lista está vacía'}
    return search_user('cedula', cedula)


@router.get('/userid/{id}')
async def user(id : str):    
   # return {usr(cedula = 98521, nombres = "Juan", apellidos = "PEREZ", direccion="Pradera")}
   #funcion de orde superior
#    resultado = filter(lambda usr: usr.cedula == ced, user_list)
#    try:
#     return list(resultado)[0]
#    except:
#     return {'La lista está vacía'}
    return search_user('_id', ObjectId(id))

# # Pedir el dato por una query    
# @router.get('/')
# async def user(ced : int):    
# #    # return {usr(cedula = 98521, nombres = "Juan", apellidos = "PEREZ", direccion="Pradera")}
# #    #funcion de orde superior
# # #    resultado = filter(lambda usr: usr.cedula == ced, user_list)
# # #    try:
# # #     return list(resultado)[0]
# # #    except:
# # #     return {'Mensaje':'No se ha encontrado al usuario'}
#      return search_user('cedula', ced)

@router.post('/',  response_model=usr, status_code=status.HTTP_201_CREATED)
async def add_user(param_usr : usr):         
      if type(search_user('cedula', param_usr.cedula)) == usr:
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'El usuario con número de cédula {param_usr.cedula} ya existe'
         )
      
      
      # crea el usuario como un diccionario
      user_dict = dict(param_usr)
      #eliminar el campo id
      del user_dict['id']
      #obtenemos el ID
      id = db_client.Ejercicio.Usuario.insert_one(user_dict).inserted_id
      
      #accedemos a la base de datos para obtener al usuario
      new_user = user_schema(db_client.Ejercicio.Usuario.find_one({'_id' : id}))
      
      # transformamos la respuesta a un Usuario y lo retornamos
      
      return usr(**new_user)
      
       
@router.put('/update', response_model = usr, status_code=status.HTTP_201_CREATED)
async def update_user(usuario : usr):   
   user_dict = dict(usuario)
   del user_dict['id']
   
   try:      
      db_client.Ejercicio.Usuario.find_one_and_replace({'_id' :  ObjectId(usuario.id)}, user_dict)
   except:
      return {'Error': 'No se ha actualizado el usuario.'}
   
   return search_user('_id', ObjectId(usuario.id))

# Cuando se crea un parametro por el path dentro del método se debe llamar igual 
@router.delete('/deletebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id : str):
   # for dato in user_list:
   #    if dato.cedula == cedula:
   #       user_list.remove(dato)   
   #       return {'Resultado' : 'Usuario eliminado'}
   #    else:
   #       return {'Resultado' : 'No existe el usuario'}
   found = db_client.Ejercicio.Usuario.find_one_and_delete({'_id' :  ObjectId(id)})
   
   if not found:
      return{'Error' : f'No existe el id {id}'}

@router.delete('/deletebycedula/{cedula}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(cedula : int):
   # for dato in user_list:
   #    if dato.cedula == cedula:
   #       user_list.remove(dato)   
   #       return {'Resultado' : 'Usuario eliminado'}
   #    else:
   #       return {'Resultado' : 'No existe el usuario'}
   found = db_client.Ejercicio.Usuario.find_one_and_delete({'cedula' : cedula})
   
   if not found:
      return{'Error' : f'No existe el id {id}'}   

# Tambien se pueden crear métodos que se usen en diferentes peticiones
# Creamos un método
def search_user(field: str, key):
    #funcion de orde superior
   #resultado = filter(lambda usr: usr.cedula == ced, user_list)
   try:
    user = db_client.Ejercicio.Usuario.find_one({field: key})
    return usr(**user_schema(user))
   except:
    return {'Mensaje':'No se ha encontrado al usuario'}