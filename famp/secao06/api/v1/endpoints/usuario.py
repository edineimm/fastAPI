from typing import List, Optional, Any
from fastapi import APIRouter, HTTPException, status, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.security import gerar_hash_senha
from models.usuario_model import UsuarioModel
from schemas.usuario_schema import UsuarioSchemaBase, UsuarioSchemaCreate, UsuarioSchemaArtigos, UsuarioSchemaUp
from core.deps import get_session, get_current_user
from core.auth import autenticar, criar_token_acesso

from sqlalchemy.exc import IntegrityError

router = APIRouter()

# GET Logado


@router.get('/logado', response_model=UsuarioSchemaBase)
def get_usuario_logado(usuario_logado: UsuarioModel = Depends(get_current_user)):
    return usuario_logado


# POST / Signup
@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuarioSchemaBase)
async def post_usuario(usuario: UsuarioSchemaCreate, db: AsyncSession = Depends(get_session)):
    novo_usuario: UsuarioModel = UsuarioModel(
        nome=usuario.nome,
        sobrenome=usuario.sobrenome,
        email=usuario.email,
        senha=gerar_hash_senha(usuario.senha),
        eh_admin=usuario.eh_admin
    )
    async with db as session:
        try:
            session.add(novo_usuario)
            await session.commit()
            return novo_usuario
        except IntegrityError:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Email já cadastrado")

# GET Usuarios


@router.get('/', response_model=List[UsuarioSchemaBase])
async def get_usuarios(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel)
        result = await session.execute(query)
        usuarios: List[UsuarioModel] = result.scalars().unique().all()
        return usuarios

# GET Usuario por ID


@router.get('/{usuario_id}', response_model=UsuarioSchemaArtigos, status_code=status.HTTP_200_OK)
async def get_usuario_por_id(usuario_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).where(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario: UsuarioSchemaArtigos = result.scalars().unique().one_or_none()
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
        return usuario

# PUT Usuario por ID


@router.put(
    '/{usuario_id}',
    response_model=UsuarioSchemaBase,
    status_code=status.HTTP_202_ACCEPTED
)
async def put_usuario(usuario_id: int, usuario: UsuarioSchemaUp, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).where(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_up: UsuarioModel = result.scalars().unique().one_or_none()
        if usuario_up:
            if usuario.nome is not None:
                usuario_up.nome = usuario.nome
            if usuario.sobrenome is not None:
                usuario_up.sobrenome = usuario.sobrenome
            if usuario.email is not None:
                usuario_up.email = usuario.email
            if usuario.senha is not None:
                usuario_up.senha = gerar_hash_senha(usuario.senha)
            if usuario.eh_admin is not None:
                usuario_up.eh_admin = usuario.eh_admin
            await session.commit()
            return usuario_up
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuário não encontrado"
            )

# DELETE Usuario por ID


@router.delete('/{usuario_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuario(usuario_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).where(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_del: UsuarioSchemaArtigos = result.scalars().unique().one_or_none()
        if not usuario_del:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
        await session.delete(usuario_del)
        await session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

# POST Login


@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    usuario = await autenticar(
        email=form_data.username, senha=form_data.password, db=db)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Email ou senha incorretos")
    token_acesso = criar_token_acesso(sub=str(usuario.id))
    return JSONResponse(content={"access_token": token_acesso, "token_type": "bearer"}, status_code=status.HTTP_200_OK)
