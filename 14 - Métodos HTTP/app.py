from flask import Flask, jsonify, request
from flask_cors import CORS
from database import db
from models import Usuario

# Cria o servidor de back-end (aplicação da web).
app = Flask(__name__)

# Habilita a resposta do back-end
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:dev%402026@localhost/loja_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/api/users", methods=["POST"])
def create_user():
    # Recupera os dados enviados pelo front-end
    data = request.get_json()
    cpf = data.get("cpf")
    nome = data.get("nome")

    if not cpf:
        return jsonify({"error":"Complete todos os campos!"}), 400
    if not nome:
        return jsonify({"error":"Complete todos os campos!"}), 400
    
    if Usuario.query.get(cpf):
        return jsonify({"error":"CPF já cadastrado!"}), 400
    
    novo_usuario = Usuario(cpf=cpf, nome=nome)
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({"cpf":novo_usuario.cpf, "nome":novo_usuario.nome}), 201
    



# ------------------------------------------------


# GET- Retorna todos os usuários cadasstrados
@app.route("/api/users", methods=["GET"])
def get_users():
    usuarios = Usuario.query.all()
    return jsonify([{"cpf" : usuario.cpf, "nome" : usuario.nome} for usuario in usuarios])


# GETpor CPF- Retorna um usuário cadasstrado
@app.route("/api/users/<string:cpf>", methods=["GET"])
def get_user(cpf):
    #Veifica se o CPF informado existe
    user = Usuario.query.get(cpf)
    if user:
        return jsonify({"cpf":user.cpf , "nome": user.nome})
    return  jsonify({"error":"Usuário não encontrado!"}), 404


# ----------------------------------

# PUT : Atualiza o nome de usuário pelo CPF
@app.route("/api/users/<string:cpf>", methods=["PUT"])
def update_user (cpf):
    data = request.get_json()
    novo_nome = data.get("nome")

    if not novo_nome:
        return jsonify({"error":"Preencha todos os campos!"}), 400
    
    user = Usuario.query.get(cpf)
    
    if user:
        user.nome = novo_nome
        db.session.commit()
        return jsonify({"cpf":user.cpf , "nome": user.nome})
    return jsonify({"error":"Usuário não encontrado..."}), 404

# DELETE - Remove um usuário pelo CPF
@app.route("/api/users/<string:cpf>", methods=["DELETE"])
def deletar_user(cpf):

    # verifica se o usuário existe
    user = Usuario.query.get(cpf)
    db.session.delete(user)
    db.session.commit()

    if user:
        return jsonify({"message":"Usuário excluído com sucesso"})
    return jsonify({"error":"Usuário não encontrado..."}), 404
    
    

#Inicia o server do back-end
if __name__ == "__main__":
    app.run(debug=True)