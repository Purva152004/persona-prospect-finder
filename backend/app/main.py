from dotenv import load_dotenv
import os

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.prospect import router

app = FastAPI(title="Persona Prospect Finder")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://persona-prospect-finders.vercel.app",  
        "http://localhost:5173"                          
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "API is running"}

app.include_router(router)
