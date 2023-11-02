#importar fastapi
from fastapi import FastAPI

#instancia de fastiAPI
app = FastAPI()

@app.get('/')
async def root():
    return {'Mensaje': 'Hola FastAPI'}

@app.get('/info')
async def root():
    return {'URL curso': 'https://ejemplo.com'}