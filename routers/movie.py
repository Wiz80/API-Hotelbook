from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import jwtBearer
from services.movie import MovieService
from schemas.movie import Movie

movieRouter = APIRouter()  # Instancia de APIRouter


# Define una ruta GET para '/movies'
@movieRouter.get('/movies',
                 tags=['movies'],
                 response_model=List[Movie],
                 status_code=200,
                 dependencies=[Depends(jwtBearer())])
def getMovies() -> List[Movie]:  # Función para obtener todas las películas
    result = MovieService().getMovies()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={"message": "No hay películas en la db"})


@movieRouter.get('/movies/{id}', tags=['movies'], response_model=Movie)
def getMovie(id: int = Path(ge=1, le=2000)) -> Movie:
    # Función para obtener una película por su ID
    result = MovieService().getMovie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movieRouter.get('/movies/', tags=['movies'], response_model=List[Movie])
def getMoviesByCategory(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:  # Función para obtener películas por su categoría
    result = MovieService().getMovieByCategory(category)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Categoría no encontrada"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movieRouter.post('/movies', tags=['movies'], response_model=dict, status_code=201)  # Ruta POST para '/movies'
def createMovie(movie: Movie) -> dict:  # Función para crear una nueva película
    statusCreateMovie = MovieService().createMovie(movie)
    if statusCreateMovie:
        return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})
    else:
        return JSONResponse(status_code=404, content={"message": statusCreateMovie})


@movieRouter.put('/movies/{id}', tags=['movies'],  response_model=dict)  # Ruta PUT para '/movies/{id}'
def updateMovie(id: int, movie: Movie) -> dict:  # Función para actualizar una película existente
    statusUpdate = MovieService().updateMovie(id, movie)
    if statusUpdate:
        return JSONResponse(status_code=201, content={"message": "Se ha modificado la película"})
    return JSONResponse(status_code=404, content={"message": "id No encontrado"})


@movieRouter.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def deleteMovie(id: int) -> dict:  # Función para eliminar una película existente
    statusDelete = MovieService().deleteMovie(id)
    if not statusDelete:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})
