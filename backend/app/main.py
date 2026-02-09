from dotenv import load_dotenv
import os

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.prospect import router

app = FastAPI(title="Persona Prospect Finder")

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from app.services.sheets_exporter import export_to_sheets

@app.get("/force-sheet-test")
def force_sheet_test():
    export_to_sheets([
        ["FINAL TEST", "SUCCESS", "CEO", "TestCo", "India", 100]
    ])
    return {"status": "done"}


app.include_router(router)
