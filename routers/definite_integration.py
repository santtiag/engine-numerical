
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from models.const import URL_ENG
from processing.definite_integration.cubic_approx import di_cubic_approximation
from processing.definite_integration.parabola import di_parabola
from processing.definite_integration.rectangle import di_rectangle
from processing.definite_integration.trapezium import di_trapezium


p_definite_integration_router = APIRouter()

@p_definite_integration_router.post(URL_ENG.home.d_i.rect, tags=['Definite Integraion'])
async def process_di_rectangle(data: dict):
    result = di_rectangle(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@p_definite_integration_router.post(URL_ENG.home.d_i.trap, tags=['Definite Integraion'])
async def process_di_trapezium(data: dict):
    result = di_trapezium(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@p_definite_integration_router.post(URL_ENG.home.d_i.para, tags=['Definite Integraion'])
async def process_di_parabola(data: dict):
    result = di_parabola(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@p_definite_integration_router.post(URL_ENG.home.d_i.ca, tags=['Definite Integraion'])
async def process_di_cubic_p_definite_integration_routerroximattion(data: dict):
    result = di_cubic_approximation(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
