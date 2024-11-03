
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from models.const import URL_ENG
from processing.interpolation.cubic_segm import i_cubic_segm
from processing.interpolation.lin_segm import i_linear_segm
from processing.interpolation.quadratic_segm import i_quadratic_segm


p_interpolation_router = APIRouter()

@p_interpolation_router.post(URL_ENG.home.inter.lin_seg, tags=['Interpolation'])
async def process_i_lin_segm(data: dict):
    result = i_linear_segm(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@p_interpolation_router.post(URL_ENG.home.inter.quad_seg, tags=['Interpolation'])
async def process_i_quadratic_segm(data: dict):
    result = i_quadratic_segm(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@p_interpolation_router.post(URL_ENG.home.inter.cub_seg, tags=['Interpolation'])
async def process_i_cubic_segm(data: dict):
    result = i_cubic_segm(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
