#importamos la librerías

from typing import Union
from fastapi import FastAPI

#creacion de la una aplicación FastAPI
app = FastAPI()

@app.get('/')
def read_root():
    #retornamos un JSON, esto es un ejemplo
    return {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
    

@app.get('/item/{item_id}')
def leer_item(item_id: int, q: Union[str, None]=None):
    return {'Item_id: ' : item_id, 'q:' : q}

@app.get('/sumando')
def suma(parametro_a: float, parametro_b: float):
    return {'La suma es:' : parametro_a+parametro_b}