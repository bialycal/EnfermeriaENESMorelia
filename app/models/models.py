from sqlalchemy import Column, String, Integer, Date, Time, ForeignKey, Enum
from .database.db import Base

class Alumno(Base):
    __tablename__ = "alumno"
    no_cuenta = Column(String(9), primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellidos = Column(String(50), nullable=False)
    semestre = Column(Integer, nullable=False)
    licenciatura = Column(String(50), nullable=False)

class Personal(Base):
    __tablename__ = "personal"
    clave_personal = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    apellidos = Column(String(50), nullable=False)
    cargo = Column(Enum('ENFERMERO', 'MEDICO'), nullable=False)

class Atencion(Base):
    __tablename__ = "atencion"
    clave_atencion = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    tipo_servicio = Column(Enum('URGENCIA', 'INSUMO', 'CONSULTA', 'OTROS'), nullable=False)
    no_cuenta = Column(String(9), ForeignKey("alumno.no_cuenta"))
    clave_personal = Column(Integer, ForeignKey("personal.clave_personal"))