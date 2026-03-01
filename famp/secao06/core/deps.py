from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from core.auth import oauth2_schema
from models.usuario_model import UsuarioModel
from core.configs import settings


""""
esse script tem a função de criar as dependências do projeto, ou seja, as funções que serão usadas como dependências em outros scripts, 
como o get_current_user, que é usada para obter o usuário atual a partir do token de acesso.
essas dependências são usadas para facilitar a reutilização de código e para garantir que as funções
sejam usadas de forma consistente em todo o projeto.
"""


class TokenData(BaseModel):
    username: Optional[str] = None


async def get_session() -> Generator:
    session: AsyncSession = Session()
    try:
        yield session
    finally:
        await session.close()


async def get_current_user(db: Session = Depends(get_session), token: str = Depends(oauth2_schema)) -> UsuarioModel:
    credentials_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET,
                             algorithms=[settings.ALGORITHM],
                             options={"verify_aud": False})
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data: TokenData = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    async with db as session:
        query = select(UsuarioModel).filter(
            UsuarioModel.id == int(token_data.username))
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()
        if usuario is None:
            raise credentials_exception
        return usuario
