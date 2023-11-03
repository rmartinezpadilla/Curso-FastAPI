from fastapi import FastAPI

app =  FastAPI()

lista_users = ['Ramón', 'David', 'Goliat']

@app.get('/users')
async def users():
    return lista_users