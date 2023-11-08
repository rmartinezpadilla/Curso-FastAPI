from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def hello():
    return {'Mensaje' : 'hello word'}