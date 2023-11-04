from fastapi import FastAPI
from routers import products, users

app  = FastAPI()

#Routers
#usamos la instancia de FastAPI "app" para llamar el Api de productos como una ruta
app.include_router(products.router)
app.include_router(users.router)


@app.get('/')
async def root():
    return {'Mensaje' : 'Hola cretino'}