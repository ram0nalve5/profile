# Importação dos módulos do SQL Alchemy.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importação da classe de banco de dados.
from Atividade.database_modeling import Usuario

# Define qual é o banco de dados
engine = create_engine("sqlite:///ecommerce.db")

# Cria uma sessão para manipulação do banco de dados.
Session = sessionmaker(bind=engine)
session = Session()

usuarios = session.query(Usuario).filter_by(id=2).first()

session.delete(usuarios)
session.commit()
session.close()
print("Usuário excluído com sucesso")
