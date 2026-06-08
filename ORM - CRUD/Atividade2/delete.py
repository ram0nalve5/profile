from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Consultas, Pacientes

engine = create_engine("sqlite:///clinica.db")

Session = sessionmaker(bind=engine)
session = Session()

consulta = session.query(Consultas).filter_by(id=3).first()
paciente = session.query(Pacientes).filter_by(id=1).first()

session.delete(consulta)
session.delete(paciente)
session.commit()
session.close()
print("Itens deletados com êxito")