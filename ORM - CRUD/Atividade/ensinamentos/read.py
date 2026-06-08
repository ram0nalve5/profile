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

# Cria uma lista com os usuários cadastrados.
usuarios = session.query(Usuario).all()

# Exibe todos os usuário.
for usuario in usuarios:
    print(usuario.id, usuario.nome, usuario.idade)

session.close()