from fastapi import FastAPI
from routers import products, users, jwt_auth_users, basic_auth_users
# importamos la clase Statics files para poder accerder a archivos dentro de nuestra API
# estos recursos son estaticos
from fastapi.staticfiles import StaticFiles


app  = FastAPI()

#Routers
#usamos la instancia de FastAPI "app" para llamar el Api de productos como una ruta
app.include_router(products.router)
app.include_router(users.router)
app.include_router(jwt_auth_users.router)
#app.include_router(basic_auth_users.router)

# Vamos a llamar a la imagen, en recursos estaticos (archivos, documentos, etc)
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/')
async def root():
    return {'Mensaje' : 'Hola cretino'}