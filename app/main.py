from fastapi import FastAPI
from .api import router as api_router

app = FastAPI()

# @app.get("/hello")
# def get_hello():
#   return {"hello": "world"}

app.include_router(api_router, prefix="/api")
