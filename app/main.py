from fastapi import FastAPI
from .routers import heroesRoute
from .database import engine
from .models import heroesModels as heroes_model

heroes_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(heroesRoute.router)