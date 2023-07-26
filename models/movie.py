from config.database import Base
from sqlalchemy import Column, Integer, String, Float


# Define la clase Movie que hereda de Base
class Movie(Base):
    __tablename__ = 'movies'  # Nombre de la tabla en la base de datos
    # Columna id, que es la clave primaria
    id = Column(Integer, primary_key=True)
    # Columna title que almacenará los títulos de las películas como strings
    title = Column(String)
    # Columna overview que almacenará las descripciones de las películas como string
    overview = Column(String)
    # Columna year que almacenará el año de las películas como enteros
    year = Column(Integer)
    # Columna rating que almacenará las calificaciones de las películas como flotantes
    rating = Column(Float)
    # Columna category que almacenará las categorías de las películas como strings
    category = Column(String)
