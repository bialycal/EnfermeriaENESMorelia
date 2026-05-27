from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.database.db import init_db
from app.routers import students, visits, staff

app = FastAPI(
    title="Enfermería ENES Morelia",
    description="Sistema de registro de visitas para la enfermería de la ENES Morelia, UNAM",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students.router, prefix="/api/students", 
tags=["Estudiantes"])
app.include_router(staff.router, prefix="/api/staff", tags=["Personal"])
app.include_router(visits.router, prefix="/api/visits", tags=["Visitas"])

app.mount("/", StaticFiles(directory="frontend", html=True), 
name="frontend")

@app.on_event("startup")
async def startup():
    init_db()
