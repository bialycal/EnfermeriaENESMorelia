from pydantic import BaseModel
from datetime import date, time
from typing import Optional
from enum import Enum

class LicenciaturaEnum(str, Enum):
    biologia = "Biología"
    geodesia = "Geodesia"
    geomatic = "Geomática"
    administracion = "Administración"
    otras = "Otras"

class AlumnoCreate(BaseModel):
    no_cuenta: str
    nombre: str
    apellidos: str
    semestre: int
    licenciatura: str

class AlumnoResponse(BaseModel):
    no_cuenta: str
    nombre: str
    apellidos: str
    semestre: int
    licenciatura: str

    class Config:
        from_attributes = True

class TipoServicio(str, Enum):
    urgencia = "URGENCIA"
    insumo = "INSUMO"
    consulta = "CONSULTA"
    otros = "OTROS"

class AtencionCreate(BaseModel):
    no_cuenta: str
    clave_personal: int
    tipo_servicio: TipoServicio

class AtencionResponse(BaseModel):
    clave_atencion: int
    fecha: date
    hora: time
    tipo_servicio: str
    no_cuenta: str
    clave_personal: int

    class Config:
        from_attributes = True
