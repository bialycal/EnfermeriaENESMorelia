from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models import Atencion, Alumno
from app.schemas import AtencionCreate, AtencionResponse
from datetime import date, datetime

router = APIRouter()

@router.post("/", response_model=AtencionResponse)
def create_visit(atencion: AtencionCreate, db: Session = Depends(get_db)):
    alumno = db.query(Alumno).filter(Alumno.no_cuenta == atencion.no_cuenta).first()
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    nueva = Atencion(
        fecha=date.today(),
        hora=datetime.now().time(),
        tipo_servicio=atencion.tipo_servicio,
        no_cuenta=atencion.no_cuenta,
        clave_personal=atencion.clave_personal
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.get("/today", response_model=list[AtencionResponse])
def get_today_visits(db: Session = Depends(get_db)):
    visitas = db.query(Atencion).filter(Atencion.fecha == date.today()).all()
    return visitas