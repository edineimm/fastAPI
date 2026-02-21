from typing import Optional
from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator("titulo")
    def validar_titulo(cls, value):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError(
                "O título do curso deve ter pelo menos três palavras.")

        if value.islower():
            raise ValueError(
                "O título do curso deve conter pelo menos uma letra maiúscula.")
        return value

    @validator("aulas")
    def validar_aulas(cls, value: int):
        if value < 12:
            raise ValueError("O número de aulas deve ser maior que 12.")

        return value

    @validator("horas")
    def validar_horas(cls, value: int):
        if value < 10:
            raise ValueError("O número de horas deve ser maior que 10.")

        return value


cursos = [
    Curso(id=1, titulo="Curso de Python", aulas=20, horas=40),
    Curso(id=2, titulo="Curso de JavaScript", aulas=25, horas=50),
    Curso(id=3, titulo="Curso de Java", aulas=30, horas=60),
    Curso(id=4, titulo="Curso de C#", aulas=15, horas=30),
]
