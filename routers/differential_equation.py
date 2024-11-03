from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from models.const import URL_ENG
from processing.diferencial_equation.linear_approx import de_linear_approx


p_differential_equation_router = APIRouter()

@p_differential_equation_router.post(URL_ENG.home.d_e.lin_approx, tags=['Methodologies'])
async def process_de_lin_approx(data: dict):
    result = de_linear_approx(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
