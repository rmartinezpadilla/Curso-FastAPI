#importar fastapi HTTP exception
from fastapi import FastAPI, HTTPException
from models.producto  import Productos
#importamos uuid para los id automaticos
from uuid import uuid4 as uuid
#importamos las excepciones HTTP


app= FastAPI()

lista_productos = []

@app.get('/')
def index():
    return {'Bienvenidos a la API de productos'}

@app.get('/productosAll')
def obtener_todos_los_productos():
    # for datos in lista_productos:
    #     return datos
    if len(lista_productos) > 0:
        return lista_productos
    else:
        return {'mensaje': 'La lista está vacía, cree un elemento para mostrar'}

@app.get('/productosID/{producto_id}')
def obtener_producto_por_id(producto_id: str):
    #forma tradicional
    
    # for p in lista_productos:
    #     if p.id_producto == producto_id:
    #         return p
    
    """usando lamba y mejorando el código"""
    resultado = list(filter(lambda p : p.id_producto == producto_id, lista_productos))
    if len(resultado) > 0:
        return resultado[0]
    
    raise HTTPException(status_code=400, detail=f'Producto con el id:{producto_id} No encontrado!')
    #return {'Mensaje': f'Producto con el id {producto_id} no encontrado'}

@app.post('/crear_producto')
def crear_producto(producto: Productos):
    producto.id_producto = str(uuid())
    lista_productos.append(producto)
    return {'Mensaje': f'Producto con el nombre:{producto.nombre_producto}  creado y agregado correctamente!'}

@app.delete('/eliminar_productos/{producto_id}')
def eliminar_producto_por_id(producto_id : str): 
    """usando lambda y mejorando el código"""
    resultado = list(filter(lambda p : p.id_producto == producto_id, lista_productos))
    if len(resultado) > 0:
        producto = resultado[0]
        lista_productos.remove(producto)
        return {'mensaje', f'El producto con el id {producto_id} ha sido eliminado correctmante'}
    
    raise HTTPException(status_code=400, detail=f'Producto con el id:{producto_id} No encontrado!')
    #return {'Mensaje': f'Producto con el id {producto_id} no encontrado'}

@app.put('/actualizar_producto/{producto_id}')
def actualizar_producto_por_id(producto_id : str, producto: Productos):
    resultado = list(filter(lambda p : p.id_producto == producto_id, lista_productos))
    if len(resultado) > 0:
        producto_encontrado = lista_productos[0]
        producto_encontrado.nombre_producto = producto.nombre_producto
        producto_encontrado.precio_compra = producto.precio_compra
        producto_encontrado.precio_venta = producto.precio_venta
        producto_encontrado.proveedor = producto.proveedor
        
        #return{'mensaje':'El producto se actualizó correctamente'}
        return producto_encontrado

        
   
    raise HTTPException(status_code=400, detail=f'No encontrado!')


"""{
  "id_producto": "string",
  "nombre_producto": "ACEITE",
  "precio_compra": 2000,
  "precio_venta": 2850,
  "proveedor": "VEGETALES"
}
"""