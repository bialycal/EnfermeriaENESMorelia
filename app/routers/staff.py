from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models import Personal
from pydantic import BaseModel
from enum import Enum

router = APIRouter()

class CargoEnum(str, Enum):
    enfermero = "ENFERMERO"
    medico = "MEDICO"

class PersonalCreate(BaseModel):
    nombre: str
    apellidos: str
    cargo: CargoEnum

class PersonalResponse(BaseModel):
    clave_personal: int
    nombre: str
    apellidos: str
    cargo: str

    class Config:
        from_attributes = True

@router.get("/", response_model=list[PersonalResponse])
def get_staff(db: Session = Depends(get_db)):
    return db.query(Personal).all()

@router.get("/{clave_personal}", response_model=PersonalResponse)
def get_staff_member(clave_personal: int, db: Session = Depends(get_db)):
    personal = db.query(Personal).filter(Personal.clave_personal == clave_personal).first()
    if not personal:
        raise HTTPException(status_code=404, detail="Personal no encontrado")
    return personal

@router.post("/", response_model=PersonalResponse)
def create_staff(personal: PersonalCreate, db: Session = Depends(get_db)):
    nuevo = Personal(**personal.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
