# Importação dos módulos do SQL Alchemy.
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base

Model = declarative_base()

class Veiculos (Model):
    __tablename__ = "Veículos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    modelo = Column(String(100), nullable=False)
    marca = Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)
    placa = Column(String(100), nullable=False, unique=True)
    proprietario = Column(String(100), nullable=False)

class Servicos (Model):
    __tablename__ = "Serviços"
    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(150), nullable=False)
    data_entrada = Column(DateTime, nullable=False)
    status = Column(String(30), nullable=False)
    valor = Column(Float, nullable=False)
    id_veiculo = Column(Integer, ForeignKey("Veículos.id"))

engine = create_engine("sqlite:///mecanico.db")
Model.metadata.create_all(engine)