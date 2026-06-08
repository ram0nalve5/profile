from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_modeling import Servicos

engine = create_engine("sqlite:///mecanico.db")

Session = sessionmaker(bind=engine)
session = Session()

servico = session.query(Servicos).filter_by(id=1).first()
servico.status = "Concluído"

session.commit()
session.close()
print("Serviço alterado com sucesso!")