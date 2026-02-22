from typing import List
from fastapi import APIRouter, HTTPException, status, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from models.curso_models import CursoModel
from core.deps import get_session

# Bypass warning SQLModel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore
# End bypass

router = APIRouter()

# nesse script temos as operações de CRUD para o curso, utilizando o SQLModel e o FastAPI.
# Cada endpoint é responsável por uma operação específica, como criar, ler, atualizar ou deletar um curso.
# O banco de dados é acessado de forma assíncrona usando o AsyncSession, e as respostas são formatadas de acordo com os modelos definidos.

# POST CURSO


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoModel)
async def post_curso(curso: CursoModel, db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(
        titulo=curso.titulo,
        aulas=curso.aulas,
        horas=curso.horas
    )

    db.add(novo_curso)
    await db.commit()

    return novo_curso

# GET Cursos


@router.get('/', response_model=List[CursoModel])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    query = select(CursoModel)
    result = await db.execute(query)
    cursos: List[CursoModel] = result.scalars().all()

    return cursos

# GET Curso


@router.get('/{curso_id}', response_model=CursoModel, status_code=status.HTTP_200_OK)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    query = select(CursoModel).where(
        CursoModel.id == curso_id)  # where or filter
    result = await db.execute(query)
    curso = result.scalar_one_or_none()

    if not curso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

    return curso

# PUT Curso


@router.put('/{curso_id}', response_model=CursoModel, status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: CursoModel, db: AsyncSession = Depends(get_session)):
    query = select(CursoModel).where(CursoModel.id == curso_id)
    result = await db.execute(query)
    curso_up: CursoModel = result.scalar_one_or_none()

    if not curso_up:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

    curso_up.titulo = curso.titulo
    curso_up.aulas = curso.aulas
    curso_up.horas = curso.horas

    await db.commit()

    return curso_up

# DELETE Curso


@router.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    query = select(CursoModel).where(CursoModel.id == curso_id)
    result = await db.execute(query)
    curso_del: CursoModel = result.scalar_one_or_none()

    if not curso_del:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

    await db.delete(curso_del)
    await db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
