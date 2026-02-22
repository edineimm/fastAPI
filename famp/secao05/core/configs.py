from pydantic import BaseSettings

# esse script é responsável por armazenar as configurações do projeto, como a URL do banco de dados e a versão da API.
# A classe Settings herda de BaseSettings, o que permite que as configurações sejam carregadas a partir de variáveis de ambiente ou arquivos de configuração.
# O objeto settings é criado a partir da classe Settings e pode ser importado em qualquer lugar do projeto para acessar as configurações.


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = 'postgresql+asyncpg://postgres:postgres@localhost:5432/faculdade'

    class config:
        case_sensitive = True


# objeto settings é global, pode ser importado em qualquer lugar do projeto para acessar as configurações.
settings = Settings()
