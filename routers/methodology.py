

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from models.const import URL_ENG
from processing.methodology.boole import m_boole
from processing.methodology.gauss import m_gauss


p_methodology_router = APIRouter()

@p_methodology_router.post(URL_ENG.home.meth.gauss, tags=['Methodologies'])
async def process_m_gauss(data: dict):
    result = m_gauss(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@p_methodology_router.post(URL_ENG.home.meth.boole, tags=['Methodologies'])
async def process_m_boole(data: dict):
    result = m_boole(data)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
