from fastapi import APIRouter

from api.v1.endpoints import curso

api_router = APIRouter()
api_router.include_router(curso.router, prefix='/cursos', tags=['Cursos'])


# nesse script, estamos definindo o roteador principal da API e incluindo o roteador específico para os cursos.
# O prefixo '/cursos' é adicionado a todas as rotas definidas no roteador de cursos, e as tags são usadas para organizar
# a documentação da API.
