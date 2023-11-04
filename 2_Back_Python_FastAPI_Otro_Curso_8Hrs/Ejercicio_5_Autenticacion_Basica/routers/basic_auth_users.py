#importamos tambien Depends
from fastapi import FastAPI, Depends
from pydantic import BaseModel
# Importamos el modulo de seguridad de fastapi
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

# Creamos instancia del sistema de autenticacion estandar de fastAPI
# le pasamos como paramtros el atributo tokenUrl = "login "---- Importante
oauth = OAuth2PasswordBearer( tokenUrl='login')

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
    'María' : {
        "username" : 'Maria',
        "full_name" : 'maría miranda',
        "email" : 'maria@hotmail.com',
        "disabled" : True,
        'password' : '987654'
    },
    'Estevan' : {
        "username" : 'estevan',
        "full_name" : 'Estevan Julio',
        "email" : 'estevan@hotmail.com',
        "disabled" : True,
        'password' : '001122'
    }
}

def searchuser(username : str):
    if username in users_db:
        return User_bd(users_db[username])
    
#Implementamos la autenticacion   
# Le pasamos como parametro en del path el mismo valor que le pusimos en la 
    # instancia de la clase OAuth2PasswordBearer, es decir, 'login'
@app.post('/login')
async def login(form : OAuth2PasswordRequestForm = Depends()):
    pass