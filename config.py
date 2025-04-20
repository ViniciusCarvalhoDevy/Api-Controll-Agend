import os
from dotenv import load_dotenv

load_dotenv()  # Carregar variáveis do .env

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")  # Pegando do .env
    SQLALCHEMY_TRACK_MODIFICATIONS = False
