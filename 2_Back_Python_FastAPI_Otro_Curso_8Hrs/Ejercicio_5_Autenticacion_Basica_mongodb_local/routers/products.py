# Importamos la clase APIRouter para poder llamar varias Api en el Main
from fastapi import APIRouter

# Agregamos el parametro prefix='/products' dentro de la instancia APIRouter para no repetirlo en cada path que se cree
#Ejemplo
"""    router =  APIRouter(prefix='/products')
"""

# Para personalizar cada api dentro de la instancia de APIRouter tambien se agregan los siguientes parametros generales
#Ejemplo
"""
router =  APIRouter(prefix='/products', tags=['Products']} )
"""

# Para generalizar una respuesta de error dentro de la API escribimos
# dentro de la instancia de APIRouter tambien se agregan los siguientes parametros generales
#Ejemplo
"""
router =  APIRouter(responses={404 : {'Mensaje' : 'No encontrado'}})
"""

# ------------------------- IMPORTANTE ---------------------
# Nos queda de la siguiente manera

router =  APIRouter(prefix='/products', tags=['Products'], responses={404 : {'message' : 'No encontrado'}})

lista_products = ['Mango', 'Fresa', 'Banano', 'lulo']

@router.get('/')
async def products():
    return lista_products

@router.get('/{name}')
async def get_product_name(name : str):
    for dato in lista_products:
        if dato == name:
            return dato
                    
@router.get('/{id}')
async def get_product_id(id : int):        
        return lista_products[id]