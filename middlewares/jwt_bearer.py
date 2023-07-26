
from starlette.requests import Request
from utils.jwt_manager import validateToken
from fastapi.security import HTTPBearer
from dotenv import load_dotenv
import os
from fastapi import HTTPException

load_dotenv()


# Define una clase jwtBearer que hereda de HTTPBearer
class jwtBearer(HTTPBearer):
    # Sobreescribe el método __call__ que se ejecuta al llamar una instancia de jwtBearer
    async def __call__(self, request: Request):
        # Obtiene el objeto autenticación que contiene las credenciales (token)
        auth = await super().__call__(request)
        # Valida el token y obtiene los datos de usuario
        data = validateToken(auth.credentials)
        user = data['user']
        # Si el correo electrónico del usuario no es os.getenv("EMAIL"), lanza una excepción HTTP con un código de estado 403
        if user['email'] != os.getenv("EMAIL"):
            raise HTTPException(status_code=403, detail="Las credenciales son invalidas")