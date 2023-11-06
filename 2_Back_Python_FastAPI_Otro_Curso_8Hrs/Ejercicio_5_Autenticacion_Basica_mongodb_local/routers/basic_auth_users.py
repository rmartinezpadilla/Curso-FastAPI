#importamos tambien Depends
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
# Importamos el modulo de seguridad de fastapi
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix='/basiccrypt', tags=['Basic Crypt'])

# Creamos instancia del sistema de autenticacion estandar de fastAPI
# le pasamos como paramtros el atributo tokenUrl = "login "---- Importante
oauth2 = OAuth2PasswordBearer( tokenUrl='login')

class Usuario(BaseModel):
    username : str
    full_name : str
    email : str
    disabled : bool
    
# Definimos una clase llamada usuario de bases de datos y esta hereda de usuario
# además se le crea un nuevo atributo, se hace de la siguiente manera

class User_bd(Usuario):
    password :  str
    
users_db = {
    'Juan' : {
        "username" : 'Juan',
        "full_name" : 'Juan Ospina',
        "email" : 'juan@hotmail.com',
        "disabled" : False,
        'password' : '123456'
    },
    'Maria' : {
        "username" : 'Maria',
        "full_name" : 'maria miranda',
        "email" : 'maria@hotmail.com',
        "disabled" : True,
        'password' : '987654'
    },
    'Estevan' : {
        "username" : 'estevan',
        "full_name" : 'Estevan Julio',
        "email" : 'estevan@hotmail.com',
        "disabled" : False,
        'password' : '001122'
    }
}

def searchuser_db(username : str):
    if username in users_db:
        return User_bd(**users_db[username])

def search_user(username : str):
    if username in users_db:
        return Usuario(**users_db[username])

async def current_user(token : str = Depends(oauth2)):
    user =  search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail='Credenciales de autenticación invalidas', 
                            headers={'WWW-Authenticate' : 'Bearer'})
    
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail='Usuario inactivo')
    return user
        

#Implementamos la autenticacion   
# Le pasamos como parametro en del path el mismo valor que le pusimos en la 
    # instancia de la clase OAuth2PasswordBearer, es decir, 'login'
@router.post('/login')
async def login(form : OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    
    if not user_db:
        raise HTTPException(status_code=400, detail='El usuario no está registrado en bases de datos')
       
    user  = searchuser_db(form.username)
    
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail='Contraseña incorrecta')
    
    return {'access_token' : user.username, 'token_type' : 'bearer'}

@router.get('/users/me')
async def me(user : Usuario = Depends(current_user)):
    return user
        
        #Video 4:54