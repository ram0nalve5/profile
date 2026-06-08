from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_modeling import Servicos

engine = create_engine("sqlite:///mecanico.db")

Session = sessionmaker(bind=engine)
session = Session()

# Cria uma lista com os usuários cadastrados.
servicos = session.query(Servicos).all()

# Exibe todos os usuário.
for servico in servicos:
    print(
        servico.id, 
        servico.descricao,
        servico.data_entrada,
        servico.status, servico.valor,
        servico.id_veiculo
    )
session.close()