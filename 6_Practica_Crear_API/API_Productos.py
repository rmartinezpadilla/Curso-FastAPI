#importar fastapi
from fastapi import FastAPI

app= FastAPI()

@app.get('/')
def index():
    return {'Bienvenidos a la página de productos'}