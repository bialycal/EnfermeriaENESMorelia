from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models import Alumno
from app.schemas import AlumnoCreate, AlumnoResponse

router = APIRouter()

@router.get("/{no_cuenta}", response_model=AlumnoResponse)
def get_student(no_cuenta: str, db: Session = Depends(get_db)):
    alumno = db.query(Alumno).filter(Alumno.no_cuenta == no_cuenta).first()
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return alumno

@router.post("/", response_model=AlumnoResponse)
def create_student(alumno: AlumnoCreate, db: Session = Depends(get_db)):
    existe = db.query(Alumno).filter(Alumno.no_cuenta == alumno.no_cuenta).first()
    if existe:
        raise HTTPException(status_code=400, detail="El alumno ya está registrado")
    nuevo = Alumno(**alumno.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

