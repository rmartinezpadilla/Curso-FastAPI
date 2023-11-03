from fastapi import FastAPI

app =  FastAPI()

lista_prodcutos = ['Mango', 'Fresa', 'Banano']

@app.get('/productos')
async def productos():
    return lista_prodcutos