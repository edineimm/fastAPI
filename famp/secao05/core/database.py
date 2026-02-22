from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine

from core.configs import settings

# esse script é responsável por configurar a conexão com o banco de dados usando SQLAlchemy.
# Ele cria um engine assíncrono e uma sessão assíncrona para interagir com o banco de dados.
# A URL do banco de dados é obtida a partir das configurações definidas no arquivo configs.py.

# O objeto Session é configurado para não cometer ou limpar automaticamente as transações,
# permitindo um controle mais preciso sobre as operações de banco de dados.

engine: AsyncEngine = create_async_engine(settings.DB_URL, echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)
