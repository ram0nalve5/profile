from sqlalchemy import create_engine, ForeignKey, Boolean, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base

Model = declarative_base()

class Sensores (Model):
    __tablename__ = "Sensores"
    id = Column(Integer, primary_key=True, autoincrement=True)
    modelo = Column(String(100), nullable=False)
    tipo = Column(String(50), nullable=False)
    ativo = Column(Boolean, default=True, nullable=False)

class Medicoes (Model):
    __tablename__ = "Medicoes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)
    tipo = Column(String(50), nullable=False)
    sensor_id = Column(Integer, ForeignKey("Sensores.id"))
    data_m = Column(DateTime, nullable=False)
    ativo = Column(Boolean, default=True, nullable=False)


engine = create_engine("sqlite:///sensores.db")
Model.metadata.create_all(engine)
print("Database criado com sucesso!")

