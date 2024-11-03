from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from models.const import URL_ENG
from processing.regression.linear import r_linear
from processing.regression.nonlinear.exponential import r_nonlinear_exponential
from processing.regression.nonlinear.polynomial import r_nonlinear_polynomial
from processing.regression.nonlinear.potential import r_nonlinear_potential


p_regression_router = APIRouter()

@p_regression_router.post(URL_ENG.home.reg.lin, tags=['Regression'])
async def process_r_linear(data: dict):
    result = r_linear(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@p_regression_router.post(URL_ENG.home.reg.nonlin.exp, tags=['Regression'])
async def process_r_nonlinear_exponential(data: dict):
    result = r_nonlinear_exponential(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@p_regression_router.post(URL_ENG.home.reg.nonlin.pot, tags=['Regression'])
async def process_r_nonlinear_potential(data: dict):
    result = r_nonlinear_potential(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@p_regression_router.post(URL_ENG.home.reg.nonlin.poly, tags=['Regression'])
async def process_r_nonlinear_polynomial(data: dict):
    result = r_nonlinear_polynomial(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
