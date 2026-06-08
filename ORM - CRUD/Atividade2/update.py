from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Pacientes, Medicos

engine = create_engine("sqlite:///clinica.db")

Session = sessionmaker(bind=engine)
session = Session()

paciente = session.query(Pacientes).filter_by(id=2).first()
paciente.telefone = "14 9912345542321"

medico = session.query(Medicos).filter_by(id=1).first()
medico.especialidade = "Radiologia"

session.commit()
session.close()
print("Dados alterados com êxito")