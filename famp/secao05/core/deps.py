from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import SessionLocal

# esse script define uma função de dependência para obter uma sessão do banco de dados.
# A função get_session é um gerador que cria uma sessão do banco de dados, as vezes chamada de "session",
# e a retorna para o código que a chamou.
# O bloco try-finally garante que a sessão seja fechada corretamente após o uso,
# mesmo que ocorra um erro durante a operação com o banco de dados.
# Isso é importante para evitar vazamentos de conexões e garantir que os recursos sejam liberados adequadamente.


async def get_session() -> Generator:

    session: AsyncSession = SessionLocal()
    try:
        yield session
    finally:
        await session.close()
