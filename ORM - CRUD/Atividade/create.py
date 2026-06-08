from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from database_modeling import Veiculos, Servicos

engine = create_engine("sqlite:///mecanico.db")

Session = sessionmaker(bind=engine)
session = Session()

v1 = Veiculos(
    modelo="Civic",
    marca="Honda",
    ano=2015,
    placa="ABC1A23",
    proprietario="João da Silva"
)

v2 = Veiculos(
    modelo="Onix",
    marca="Chevrolet",
    ano=2020,
    placa="XYZ9B88",
    proprietario="Maria de Souza"
)

s1 = Servicos(
    descricao="Troca de óleo",
    data_entrada=datetime(2026, 3, 1),
    status="Em andamento",
    valor=150.00,
    id_veiculo=1
)

s2 = Servicos(
    descricao="Alinhamento e balanceamento",
    data_entrada=datetime(2026, 3, 1),
    status="Pendente",
    valor=120.00,
    id_veiculo=1
)

s3 = Servicos(
    descricao="Troca de pastilhas de freio",
    data_entrada=datetime(2026, 3, 2),
    status="Em andamento",
    valor=300.00,
    id_veiculo=2
)

s4 = Servicos(
    descricao="Revisão elétrica",
    data_entrada=datetime(2026, 3, 2),
    status="Cancelado",
    valor=200.00,
    id_veiculo=2
)

session.add_all([v1, v2, s1, s2, s3, s4])
session.commit()
session.close()

print("Veículo(s) e Serviço(s) cadastrado(s) com sucesso!")