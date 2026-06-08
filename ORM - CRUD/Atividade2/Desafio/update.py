from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_sensores import Sensores, Medicoes
from datetime import datetime

engine = create_engine("sqlite:///sensores.db")

Session = sessionmaker(bind=engine)
session = Session()

opcao = int(input("Digite: \n1 - para alterar um sensor \n2 - para alterar uma medição \n3 - para sair\n"))
if opcao == 1:
    try:
        id_s = int(input("Digite o ID do sensor a alterar: "))
        sensor = session.query(Sensores).filter_by(id=id_s).first()
        alteracao = int(input("Digite: \n1 - para alterar o modelo \n2 - para alterar o tipo\n"))
        if alteracao == 1:
            modelo = str(input("Digite o novo modelo: "))
            sensor.modelo = modelo
            print("Modelo alterado com sucesso!")
        elif alteracao == 2:
            tipo = str(input("Digite o novo tipo do sensor:"))
            sensor.tipo = tipo
            print("Tipo alterado com sucesso!")
        else:
            print("Opção inválida!")
    except ValueError:
        print("Valor de dado incorreto!")
elif opcao == 2:
    try:
        id_m = int(input("Digite o ID da medição a alterar: "))
        medicao = session.query(Medicoes).filter_by(id=id_m).first()
        alteracao = int(input("Digite: \n1 - para alterar o valor \n2 - para alterar o tipo \n3 - para alterar o ID do sensor \n4 - para alterar a data \n"))
        match(alteracao):
            case 1:
                valor = str(input("Digite o novo valor: "))
                medicao.valor = valor
                print("Valor alterado com sucesso!")
            case 2:
                tipo = str(input("Digite o novo tipo da medição:"))
                medicao.tipo = tipo
                print("Tipo alterado com sucesso!")
            case 3:
                sensor_id = int(input("Digite o novo id do sensor: "))
                medicao.sensor_id = sensor_id
            case 4:
                data_m = datetime.strptime(input("Digite o dia e o horário da medição (AAAA-M-D) (HH:MM:SS): "), "%Y-%m-%d %H:%M:%S")
                medicao.data_m = data_m

            case _:
                print("Opção inválida!")
    except ValueError:
        print("Valor de dado incorreto!")
elif opcao == 3:
    print("Saindo...")
else:
    print("Opção inválida!")

session.commit()
session.close()