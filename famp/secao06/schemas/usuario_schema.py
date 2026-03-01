from typing import Optional, List
from pydantic import BaseModel, EmailStr, constr
from schemas.artigo_schema import ArtigoSchema


class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False

    class Config:
        from_attributes = True


class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: constr(min_length=8)


class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]


class UsuarioSchemaUp(BaseModel):
    nome: Optional[str] = None
    sobrenome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[constr(min_length=8)] = None
    eh_admin: Optional[bool] = None

    class Config:
        from_attributes = True
