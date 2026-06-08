from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from database_sensores import Sensores, Medicoes

engine = create_engine("sqlite:///sensores.db")

Session = sessionmaker(bind=engine)
session = Session()

opcao = int(input("Digite: \n1 - para cadastrar um sensor \n2 - para cadastrar uma medição \n3 - para sair\n"))
if opcao == 1:
    try:

        modelo = str(input("Digite o modelo do sensor: "))
        tipo = str(input("Digite o tipo do sensor: "))
        sensor = Sensores(modelo=modelo, tipo=tipo)
        session.add(sensor)
        session.commit()
        print("Sensor cadastrado com sucesso!")
    except ValueError:
        print("Valor de dado incorreto!")
elif opcao == 2:
    try:
        valor = float(input("Digite o valor da medição: "))
        tipo = str(input("Digite o tipo do dado: "))
        sensor_id = int(input("Digite o ID do sensor: "))
        data_m = datetime.strptime(input("Digite o dia e o horário da medição (AAAA-M-D) (HH:MM:SS) "), "%Y-%m-%d %H:%M:%S")
        medicao = Medicoes(
            valor=valor,
            tipo=tipo,
            sensor_id=sensor_id,
            data_m=data_m)
        session.add(medicao)
        session.commit()
        print("Medição cadastrada com sucesso!")
    except ValueError:
        print("Valor de dado incorreto!")
elif opcao == 3:
    print("Saindo...")
else:
    print("Opção inválida!")
session.close()
