
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)

    # Método que será invocado para cada solicitud
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        # Intenta procesar la solicitud
        try:
            return await call_next(request)
        # Si se produce una excepción, la captura y devuelve una respuesta JSON con el error
        except Exception as e:
            return JSONResponse(status_code=500, content={"Error": str(e)})
