from pydantic import BaseModel
from typing import Optional


class ArtigoSchemaBase(BaseModel):
    titulo: str
    descricao: str
    url_fonte: str


class ArtigoSchemaCreate(ArtigoSchemaBase):
    pass  # usado para POST


class ArtigoSchemaUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    url_fonte: Optional[str] = None


class ArtigoSchema(ArtigoSchemaBase):
    id: Optional[int]
    usuario_id: Optional[int]

    class Config:
        from_attributes = True
