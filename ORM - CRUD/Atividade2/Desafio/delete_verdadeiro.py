from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_sensores import Sensores, Medicoes

engine = create_engine("sqlite:///sensores.db")

Session = sessionmaker(bind=engine)
session = Session()

opcao = int(input("Digite: \n1 - para excluir um sensor \n2 - para excluir uma medição \n3 - para sair\n"))
if opcao == 1:
    id_s = int(input("Digite o ID do sensor a deletar: "))
    sensor = session.query(Sensores).filter_by(id=id_s).first()
    session.delete(sensor)
    session.commit()
    print("Sensor deletado com sucesso!")
elif opcao == 2:
    id_m = int(input("Digite o ID da medição a deletar: "))
    medicao = session.query(Medicoes).filter_by(id=id_m).first()
    session.delete(medicao)
    session.commit()
    print("Medição deletada com sucesso!")
else:
    print("Saindo...")
session.close