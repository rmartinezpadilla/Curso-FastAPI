from fastapi import APIRouter

router_user = APIRouter()


@router_user.get('/users')
async def hello():
    return {'Mensaje' : 'hello word'}