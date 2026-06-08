from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_modeling import Servicos

# Define qual é o banco de dados
engine = create_engine("sqlite:///mecanico.db")

Session = sessionmaker(bind=engine)
session = Session()

servico = session.query(Servicos).filter_by(status="Cancelado").first()

session.delete(servico)
session.commit()
session.close()
print("Serviço excluído com sucesso")
