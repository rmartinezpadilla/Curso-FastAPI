# Creamos esta clase para poder tomar la consulta de la base de datos y convertirla en un objteo de tipo  Usuario

def user_schema(user) -> dict:
    return {
            'id': str(user['_id']),
            'cedula': user['cedula'],
            'nombres': user['nombres'],
            'apellidos': user['apellidos'],
            'direccion': user['direccion'],
            }

#declaramos una funcion para devolver varios registros
def users_schema(users) -> list:
    return [user_schema(user) for user in users]