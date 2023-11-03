#importar fastapi
from fastapi import FastAPI

#instancia de fastiAPI
app = FastAPI()

#Iniciar el servidor: uvicorn archivo:app --reload
#Detener el servidor: CTRL + C

@app.get('/')
async def root():
    return {'Mensaje': 'Hola FastAPI'}

@app.get('/url')
async def url():
    return {'URL': 'https://ejemplo.com'}

#documentacion Swagger: http://127.0.0.1:8000/docs
#documentacion Redocly: http://127.0.0.1:8000/redoc