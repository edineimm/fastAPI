from typing import List, Optional
from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import Curso

app = FastAPI()

cursos = {
    1: {
        "titulo": "Fundamentos de Python",
        "aulas": 10,
        "horas": 20
    },
    2: {
        "titulo": "Fundamentos de FastAPI",
        "aulas": 15,
        "horas": 30
    }
}


@app.get("/cursos")
async def get_cursos():
    return cursos


@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int):

    try:
        curso = cursos[curso_id]
        curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Optional[Curso] = None):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso


@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


@app.delete("/cursos/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
