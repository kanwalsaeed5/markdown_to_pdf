from fastapi import FastAPI
from app.routes import convert

app = FastAPI()

app.include_router(convert.router)
