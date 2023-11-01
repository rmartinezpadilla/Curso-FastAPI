#importamos la clase date para el tipo de datos de las fechas
from datetime import date

#improtamos Base model para las clases
from pydantic import BaseModel


# creamos una funcion tipo main con un parametro de tipo string
def main(user_id: str):
    return user_id


# creamos un modelo con pydantic
class User(BaseModel):
    id: int
    name: str
    joined: date

# primera forma de como crear le objeto
# pasando todos los parametros al constructor de la clase
my_user: User = User(id=3, name="John Doe", joined="2018-07-19")

print(my_user)

# segunda forma de como crear el objeto como un diccionario
second_user_data = {
    "id": 4,
    "name": "Mary",
    "joined": "2018-11-30",
}

my_second_user: User = User(**second_user_data)
print(second_user_data)