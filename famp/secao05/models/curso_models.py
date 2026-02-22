from typing import Optional
from sqlmodel import SQLModel, Field

# esse script é o modelo de dados do curso, ou seja, a estrutura da tabela no banco de dados


class CursoModel(SQLModel, table=True):

    __tablename__: str = "cursos"

    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    aulas: int
    horas: int
