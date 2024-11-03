from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.interpolation import p_interpolation_router
from routers.regression import p_regression_router
from routers.definite_integration import p_definite_integration_router
from routers.methodology import p_methodology_router
from routers.differential_equation import p_differential_equation_router

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

app.include_router(p_interpolation_router)
app.include_router(p_regression_router)
app.include_router(p_definite_integration_router)
app.include_router(p_methodology_router)
app.include_router(p_differential_equation_router)
