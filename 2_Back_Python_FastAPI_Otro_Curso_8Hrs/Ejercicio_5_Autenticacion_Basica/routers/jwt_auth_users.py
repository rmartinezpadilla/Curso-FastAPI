#importamos tambien Depends
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
# Importamos el modulo de seguridad de fastapi
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = '5b1638be027fe9f7904b6a1b55838674'

router = APIRouter(prefix='/crypt', tags=['Encriptacion JWT'])

# Creamos instancia del sistema de autenticacion estandar de fastAPI
# le pasamos como paramtros el atributo tokenUrl = "login "---- Importante
oauth2 = OAuth2PasswordBearer( tokenUrl='login')

crypt = CryptContext(schemes=["bcrypt"])

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
        'password' : '$2a$12$dAf3E3bkv81Mfwcw2xD.y.XCifAkVOFkb1AyU0rLDywAUOhdpW.6i'
    },
    'Maria' : {
        "username" : 'Maria',
        "full_name" : 'maría miranda',
        "email" : 'maria@hotmail.com',
        "disabled" : True,
        'password' : '$2a$12$qznF18zyLLbyqKH9gETN7.Epa/ESPCtMgjKmy/94f07hbCXq6MZgm'
    },
    'Estevan' : {
        "username" : 'Estevan',
        "full_name" : 'Estevan Julio',
        "email" : 'estevan@hotmail.com',
        "disabled" : False,
        'password' : '$2a$12$fbMBNRnDr/zeYS9p6hwIqeitKusiMj6RAqjRm9uMmgdQZAyRIA/w.'
    }
}

def searchuser_db(username : str):
    if username in users_db:
        return User_bd(**users_db[username])

def search_user(username : str):
    if username in users_db:
        return Usuario(**users_db[username]) 
        
#Implementamos la autenticacion   
# Le pasamos como parametro en del path el mismo valor que le pusimos en la 
    # instancia de la clase OAuth2PasswordBearer, es decir, 'login'
@router.post('/login')
async def login(form : OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    
    if not user_db:
        raise HTTPException(status_code=400, detail='El usuario no está registrado en bases de datos')
       
    user  = searchuser_db(form.username)
    
    crypt.verify(form.password, user.password)
    
    if not crypt:
        raise HTTPException(status_code=400, detail='Contraseña incorrecta')
    
    expire_token  = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    
    acces_token = {
        'sub' : user.username,
        'exp' :expire_token
    }   
        
    return {'access_token' : jwt.encode(acces_token, SECRET, algorithm=ALGORITHM), 'token_type' : 'bearer'}

async def auth_user(token : str = Depends(oauth2)):    
    try:
        user_name =  jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get('sub')
        
        if user_name is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                detail='usuario vacio', 
                headers={'WWW-Authenticate' : 'Bearer'})        
    except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                detail='Credenciales de autenticación invalidas o token vencido', 
                headers={'WWW-Authenticate' : 'Bearer'})
    
    return search_user(user_name)
    

async def current_user(user : Usuario = Depends(auth_user)):
    
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail='Usuario inactivo')
    return user

@router.get('/users/me')
async def me(user : Usuario = Depends(current_user)):
    return user