#importar fastapi
from fastapi import FastAPI
from models.producto  import Productos

app= FastAPI()

lista_productos = []

@app.get('/')
def index():
    return {'Bienvenidos a la API de productos'}

@app.get('/producto')
def obtener_producto():
    return lista_productos

@app.post('/producto')
def crear_producto(producto: Productos):
    lista_productos.append(producto)
    return 'Producto creado y agregado correctamente!'