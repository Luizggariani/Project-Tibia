# config.py

from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configurações de conexão com o banco de dados
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "Tibia")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "user")
DB_PORT = os.getenv("DB_PORT", "5432")

# URLs da API TibiaData
TIBIA_API_BASE_URL = "https://api.tibiadata.com/v4"
CREATURES_ENDPOINT = f"{TIBIA_API_BASE_URL}/creatures"

# Informações do banco de dados
DB_SCHEMA = "tibia_api"
CREATURES_TABLE = "creatures"

# Configurações extras (exemplo para embeddings)
EMBEDDING_DIMENSION = 384
