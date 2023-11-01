# FastAPI es uno de los frameworks para la creación de aplicaciones webs Python más populares en este momento, 
# haciendo competencia a Frameworks con mucho más recorrido como Django o Flask, 
# creando una muy buena comunidad a su alrededor, algo que no había hecho ningún otro 
# Framework de Python hasta el momento.

# Dependencias en FastAPI
# FastAPI nos ayuda con esta tarea de gestión de dependencias de forma completamente nativa, 
# incluyéndola en el Framework de Python.

"""
from fastapi  import FastAPI

app = FastAPI()

def get_hello() -> str:
    return 'hello'

@app.route('/hello_world')
def hello_world(d: str = Depends(get_hello)):
    return d + ' world'
    
    """

def poner_primeras_mayusculas(text_1: str, text_2:str):
    return f"{text_1.capitalize()}, {text_2.capitalize()}"

print(poner_primeras_mayusculas('ruben', 'martinez'))