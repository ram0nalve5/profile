from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker

from database import Pacientes, Medicos, Consultas
engine = create_engine ("sqlite:///clinica.db")

Session = sessionmaker(bind=engine)
session = Session()

p1 = Pacientes(nome="Camilla Souza", telefone="14 99189-4359")
p2 = Pacientes(nome="Ricardo da Silva", telefone="14 99888-4959")

m1 = Medicos (nome="Rufus Almeida", especialidade="pediatra")
m2 = Medicos (nome="Noah Nascimento", especialidade="cirurgião")

c1 = Consultas (data=datetime(2026, 10 , 12), id_paciente=1, id_medico=2)
c2 = Consultas (data=datetime(2026, 8, 11), id_paciente=2, id_medico=1)
c3 = Consultas (data=datetime(2026, 11, 1), id_paciente=2, id_medico=2)


session.add_all([p1, p2, m1, m2, c1, c2, c3])

session.commit()
session.close()

print("Dados cadastrados")