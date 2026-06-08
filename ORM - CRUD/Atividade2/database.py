from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Model = declarative_base()

class Pacientes (Model):
    __tablename__ = "Pacientes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(20))

class Medicos (Model):
    __tablename__ = "Medicos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    especialidade = Column(String(100), nullable=False)

class Consultas (Model):
    __tablename__ = "Consultas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DateTime, nullable=False)
    id_paciente = Column(Integer, ForeignKey("Pacientes.id"))
    id_medico = Column(Integer, ForeignKey("Medicos.id"))


engine = create_engine("sqlite:///clinica.db")
Model.metadata.create_all(engine)

