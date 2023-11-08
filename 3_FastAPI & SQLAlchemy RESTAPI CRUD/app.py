from fastapi import FastAPI
from routers.user import router_user

app = FastAPI()
app.include_router(router_user)