from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=["argon2"], deprecated="auto")


def verificar_senha(senha: str, senha_hash: str) -> bool:
    """"
    Verifica se a senha fornecida corresponde ao hash armazenado.
    """
    return CRIPTO.verify(senha, senha_hash)


def gerar_hash_senha(senha: str) -> str:
    """"
    Gera um hash seguro para a senha fornecida.
    """
    return CRIPTO.hash(senha)
