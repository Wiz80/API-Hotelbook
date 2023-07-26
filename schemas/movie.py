from pydantic import BaseModel, Field
from typing import Optional


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=30)
    overview: str = Field(min_length=5, max_length=130)
    year: int = Field(le=2023)
    rating: float = Field(default=10, ge=1, le=10)
    category: str = Field(default='Categoría', min_length=4, max_length=15)

    class Config:  # Configuración adicional para el modelo Pydantic
        schema_extra = {
            # Esquema adicional para la generación de documentación automática
            "example": {
                # Proporciona un ejemplo de cómo se debe formatear un objeto Movie
                "id": 1,
                "title": "Mi película",
                "overview": "Descripción de la película",
                "year": 2022,
                "rating": 9.8,
                "category": "Acción"
            }
        }
