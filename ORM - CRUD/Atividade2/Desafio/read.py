from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_sensores import Sensores, Medicoes

engine = create_engine("sqlite:///sensores.db")

Session = sessionmaker(bind=engine)
session = Session()

sensores = session.query(Sensores).all()
medicoes = session.query(Medicoes).all()

# Exibe todos os usuário.
print("________________________Sensores:___________________\n")
for sensor in sensores:
    if sensor.ativo:
        print(
            f"ID: {sensor.id}\n"
            f"Modelo: {sensor.modelo}\n"
            f"Tipo: {sensor.tipo}"
            "\n____________________________________________________\n"
        )
print("________________________Medições:___________________\n")
for medicao in medicoes:
    if medicao.ativo:
        print(
            f"ID: {medicao.id}\n"
            f"Valor: {medicao.valor}\n"
            f"Tipo: {medicao.tipo}\n"
            f"Id do Sensor: {medicao.sensor_id}\n"
            f"Data da Medição: {medicao.data_m}"
            "\n____________________________________________________\n"
        )

session.close()