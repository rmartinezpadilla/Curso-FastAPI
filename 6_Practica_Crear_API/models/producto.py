from typing import Optional
from pydantic import BaseModel

class Productos(BaseModel):
    id_producto : Optional[str]
    nombre : str
    precio_compra : float
    precio_venta: float


