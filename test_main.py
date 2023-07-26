from fastapi.testclient import TestClient
from main import app
import pytest
from schemas.movie import Movie

client = TestClient(app)


def testHome():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == '<h1>Hello world</h1>'


def testLogin():
    response = client.post(
        "/login", json={"email": "admin@gmail.com", "password": "admin"})
    assert response.status_code == 200
    assert isinstance(response.json(), str) and response.json() != ""


@pytest.mark.parametrize("id", [5, 6, 7])
def testGetMovie(id: int):
    response = client.get(f"/movies/{id}")
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["id"] == id


@pytest.mark.parametrize("category", ["Comedia", "Acción", "Drama"])
def testGetMoviesByCategory(category):
    response = client.get("/movies/", params={"category": category})
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def testCreateMovie():
    movie = Movie(title="Elementos 2", year=2023, category="Acción",
                  overview="Una película de acción", rating=7.1)
    response = client.post("/movies", json=dict(movie))
    assert response.status_code == 201
    assert "message" in response.json()
    assert response.json()["message"] == "Se ha registrado la película"


def testUpdateMovie():
    movie_id = 7
    movie = Movie(title="Donny Darko", year=2023, category="Acción",
                  overview="Una película de acción actualizada", rating=7.1)
    response = client.put(f"/movies/{movie_id}", json=dict(movie))
    assert response.status_code == 201
    assert "message" in response.json()
    assert response.json()["message"] == "Se ha modificado la película"
