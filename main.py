from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base

from middlewares.error_handler import ErrorHandler
from routers.movie import movieRouter
from routers.users import userRouter

app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)


Base.metadata.create_all(bind=engine)
app.include_router(movieRouter)
app.include_router(userRouter)


# endpoint decorator to define the path of this function as "/"
@app.get("/", tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')
