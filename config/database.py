import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()  # Carga las variables de entorno desde el archivo .env

database_name = os.getenv("DATABASE_NAME")
username = os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")

# Formato de la cadena de conexión para PostgreSQL
databaseUrl = f"postgresql://{username}:{password}@{host}:{port}/{database_name}"

engine = create_engine(databaseUrl, echo=True)

session = sessionmaker(bind=engine)

Base = declarative_base()
