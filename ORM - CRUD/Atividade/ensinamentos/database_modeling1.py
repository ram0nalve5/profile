# Importação dos módulos do SQL Alchemy.
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

Model = declarative_base()

class Usuario (Model):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    idade = Column(Integer)

engine = create_engine("sqlite:///mecanico.db")
Model.metadata.create_all(engine)