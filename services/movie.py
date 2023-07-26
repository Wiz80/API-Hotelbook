from models.movie import Movie as MovieModel
from config.database import session
from schemas.movie import Movie
from config.redis import getRedisConnection
import pickle

db = session()


class MovieService():

    def getMovies(self):
        connection = getRedisConnection()
        result = connection.get("movies")
        if result is None:  # If the cache does not contain the data
            # Get data from database
            result = db.query(MovieModel).all()

            # Store the data in the cache for future access,
            # first converting the data to bytes
            connection.set("movies", pickle.dumps(result))
        else:
            # If the cache contains the data, convert it back to Python objects
            result = pickle.loads(result)
        return result

    def getMovie(self, id):
        connection = getRedisConnection()
        key = "movies:" + str(id)
        result = connection.get(key)
        if result is None:  # If the cache does not contain the data
            # Get data from database
            result = db.query(MovieModel).filter(MovieModel.id == id).first()

            # Store the data in the cache for future access
            connection.set(key, pickle.dumps(result))
        else:
            # If the cache contains the data, convert it back to Python objects
            result = pickle.loads(result)

        return result

    def getMovieByCategory(self, category):
        connection = getRedisConnection()
        key = "movies:" + category
        # Try to get the data from the cache first
        result = connection.get(key)
        if result is None:  # If the cache does not contain the data
            # Get data from database
            result = db.query(MovieModel).filter(
                MovieModel.category == category).all()

            # Store the data in the cache for future access
            connection.set(key, pickle.dumps(result))
        else:
            # If the cache contains the data, convert it back to Python objects
            result = pickle.loads(result)

        return result

    def createMovie(self, movie: Movie):
        connection = getRedisConnection()
        try:
            newMovie = MovieModel(**dict(movie))
            db.add(newMovie)
            db.commit()
            # After successful creation, invalidate the 'movies' cache
            connection.delete("movies")

            # If the category list is cached, also invalidate that
            connection.delete("movies:" + newMovie.category)
            return True
        except Exception as e:
            return e

    def updateMovie(self, id: int, data: Movie):
        connection = getRedisConnection()
        result = db.query(MovieModel).filter(MovieModel.id == id).first()
        if not result:
            return False
        old_category = result.category

        result.title = data.title
        result.overview = data.overview
        result.year = data.year
        result.rating = data.rating
        result.category = data.category
        db.commit()
        # After successful update, invalidate the 'movies' cache
        connection.delete("movies")

        # If the old or new category lists are cached, invalidate them
        connection.delete("movies:" + old_category)
        connection.delete("movies:" + data.category)

        return True

    def deleteMovie(self, id):
        connection = getRedisConnection()
        result = db.query(MovieModel).filter(MovieModel.id == id).first()
        if not result:
            return False
        old_category = result.category
        db.delete(result)
        db.commit()
        # After successful deletion, invalidate the 'movies' cache
        connection.delete("movies")

        # If the category list is cached, invalidate that
        connection.delete("movies:" + old_category)
        connection.delete("movies:" + str(id))
        return True
