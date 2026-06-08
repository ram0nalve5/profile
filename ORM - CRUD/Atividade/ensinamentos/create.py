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

#Cria dois usuários (objetos).
u1 = Usuario(
    nome="Nicolas Mohammed",
    email="nicolas@gmail.com",
    idade=67
    )

u2 = Usuario(
    nome="Jerivaldo",
    email="jerivaldo@gmail.com",
    idade=12
    )

# Adiciona os users ao banco de dados
session.add(u1)
session.add(u2)

# Confirma as operações de banco de dados
session.commit()
session.close()

#Feedback para usuário
print("Usuários criados com sucesso!")