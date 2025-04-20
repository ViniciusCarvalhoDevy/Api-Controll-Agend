import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv, set_key

# Carregar variáveis do .env
load_dotenv()

ENV_FILE = ".env"
KEY_NAME = "FERNET_SECRET_KEY"

def generate_key():
    """Gera uma chave e salva no arquivo .env, se não existir."""
    if not os.getenv(KEY_NAME):
        key = Fernet.generate_key().decode()
        set_key(ENV_FILE, KEY_NAME, key)
        print("Nova chave gerada e salva no .env!")
    else:
        print("Chave já existe no .env.")

def load_key():
    """Carrega a chave do .env"""
    key = os.getenv(KEY_NAME)
    if key:
        return key.encode()
    else:
        raise FileNotFoundError("Chave de criptografia não encontrada no .env! Execute 'generate_key()' primeiro.")

# Executar a geração da chave apenas uma vez
generate_key()
