from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Pacientes, Medicos, Consultas

engine = create_engine ("sqlite:///clinica.db")

Session = sessionmaker(bind=engine)
session = Session()

pacientes = session.query(Pacientes).all()
medicos = session.query(Medicos).all()
consultas = session.query(Consultas).all()

for paciente in pacientes:
    print(paciente.id, paciente.nome, paciente.telefone)

for medico in medicos:
    print(medico.id, medico.nome, medico.especialidade)

for consulta in consultas:
    print(consulta.data, consulta.id_paciente, consulta.id_medico)
session.close()