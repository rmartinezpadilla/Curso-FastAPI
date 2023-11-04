from fastapi import FastAPI
from routers import products, users
# importamos la clase Statics files para poder accerder a archivos dentro de nuestra API
# estos recursos son estaticos
from fastapi.staticfiles import StaticFiles


app  = FastAPI()

#Routers
#usamos la instancia de FastAPI "app" para llamar el Api de productos como una ruta
app.include_router(products.router)
app.include_router(users.router)

# Vamos a llamar a la imagen, en recursos estaticos (archivos, documentos, etc)
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/')
async def root():
    return {'Mensaje' : 'Hola cretino'}