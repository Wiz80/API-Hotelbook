from fastapi import APIRouter
from utils.jwt_manager import createToken
from fastapi.responses import JSONResponse
from schemas.users import User
from dotenv import load_dotenv
import os

userRouter = APIRouter()  # Crea una nueva instancia de APIRouter
load_dotenv()


@userRouter.post('/login', tags=['auth'])
def login(user: User):
    # Si el correo electrónico y la contraseña del usuario son correctos
    if user.email == os.getenv("EMAIL") and user.password == os.getenv("PASSWORD"):
        # Crea un token JWT
        token: str = createToken({'id': 'admin', 'user': dict(user)})
    # Devuelve una respuesta JSON con el token JWT
    return JSONResponse(status_code=200, content=token)
