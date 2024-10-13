from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from pandas.io.parquet import json

from processing.definite_integration.cubic_approximation import di_cubic_approximation
from processing.definite_integration.parabola import di_parabola
from processing.definite_integration.rectangle import di_rectangle
from processing.definite_integration.trapezium import di_trapezium
from processing.interpolation.cubic_segm import i_cubic_segm
from processing.interpolation.lin_segm import i_linear_segm
from processing.interpolation.quadratic_segm import i_quadratic_segm
from processing.regression.linear import r_linear
from processing.regression.nonlinear.exponential import r_nonlinear_exponential
from processing.regression.nonlinear.polynomial import r_nonlinear_polynomial
from processing.regression.nonlinear.potential import r_nonlinear_potential

from models.urls import URL

# INFO: Processing

app = FastAPI()
app.title = 'Processing'

origins = [
    "https://api-numerical.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
    expose_headers=["Content-Type", "Authorization"],
    max_age=3600,  # tiempo de vida de la configuración CORS (en segundos)
)

url_eng = URL('/engine')

# INFO: INTERPOLATION
@app.post(url_eng.home.inter.lin_seg, tags=['Interpolation'])
async def process_i_lin_segm(data: dict):
    result = i_linear_segm(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@app.post(url_eng.home.inter.quad_seg, tags=['Interpolation'])
async def process_i_quadratic_segm(data: dict):
    result = i_quadratic_segm(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@app.post(url_eng.home.inter.cub_seg, tags=['Interpolation'])
async def process_i_cubic_segm(data: dict):
    result = i_cubic_segm(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


# INFO: REGRESSION
@app.post(url_eng.home.reg.lin, tags=['Regression'])
async def process_r_linear(data: dict):
    result = r_linear(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@app.post(url_eng.home.reg.nonlin.exp, tags=['Regression'])
async def process_r_nonlinear_exponential(data: dict):
    result = r_nonlinear_exponential(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@app.post(url_eng.home.reg.nonlin.pot, tags=['Regression'])
async def process_r_nonlinear_potential(data: dict):
    result = r_nonlinear_potential(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@app.post(url_eng.home.reg.nonlin.poly, tags=['Regression'])
async def process_r_nonlinear_polynomial(data: dict):
    result = r_nonlinear_polynomial(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


# DEFINITE INTEGRATION
@app.post(url_eng.home.d_i.rect, tags=['Definite Integraion'])
async def process_di_rectangle(data: dict):
    result = di_rectangle(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@app.post(url_eng.home.d_i.trap, tags=['Definite Integraion'])
async def process_di_trapezium(data: dict):
    result = di_trapezium(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@app.post(url_eng.home.d_i.para, tags=['Definite Integraion'])
async def process_di_parabola(data: dict):
    result = di_parabola(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@app.post(url_eng.home.d_i.ca, tags=['Definite Integraion'])
async def process_di_cubic_approximattion(data: dict):
    result = di_cubic_approximation(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
