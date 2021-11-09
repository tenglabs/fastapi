from . import models
from .database import engine
from fastapi import FastAPI
from . import routes

app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(routes.router)


