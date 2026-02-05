from fastapi import FastAPI
from app.routes.prospect import router

app = FastAPI(title="Persona Prospect Finder")

app.include_router(router)
