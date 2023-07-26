import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from dotenv import load_dotenv

load_dotenv()  # Carga las variables de entorno desde el archivo .env

database_name = os.getenv("DATABASE_NAME")
username = os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")

# Formato de la cadena de conexión para PostgreSQL
databaseUrl = f"postgresql://{username}:{password}@{host}:{port}/{database_name}"

# Crea una instancia de Engine que proporciona una fuente de conectividad a la base de datos especificada
engine = create_engine(databaseUrl, echo=True)

# Configura la clase de sesión a utilizar con un enlace de motor específico
session = sessionmaker(bind=engine)
