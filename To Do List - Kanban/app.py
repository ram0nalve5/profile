	# Importa o Flask para criar a aplicação da web.
from flask import Flask, request, jsonify

# Importa o objeto de manipulação do banco de dados.
from database import db

# Importa as classes/tabelas de banco de dados.
from models import Usuario, StatusTarefa, Tarefa

# Importa a biblioteca para criptografar senhas.
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

# Importa a biblioteca que faz interação com o back-end.
from flask_cors import CORS

# Importa a biblioteca para autenticação de Token da Web (JWT).
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt

# Importa a biblioteca para manipular datas.
from datetime import timedelta

# Importa os módulos para manipular variáveis de ambiente.
from dotenv import load_dotenv
import os

# Cria a aplicação da web.
app = Flask(__name__)

# Define que o frontend possa requisitar recursos do backend.
CORS(app)

# Carrega as variáveis de ambiente (.env).
load_dotenv()

# Configura o banco de dados MySQL.
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Configura o Token da Web (JWT).
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=8)

# Inicializa o gerenciador de Tokens da Web (JWT).
jwt = JWTManager(app)

# Vincula o banco de dados à aplicação da web.
db.init_app(app)

# Cria as tabelas de banco de dados, caso não existam.
with app.app_context():

    db.create_all()

    # Insere o administrador caso não exista.
    if not Usuario.query.filter_by(cpf="123.456.789-10").first():

        master = Usuario(
            nome="Administrador",
            cpf="123.456.789-10",
            email="administrador@email.com",
            senha=generate_password_hash("123456"),
            administrador=True
        )

        db.session.add(master)
        db.session.commit()


# Rota para login de usuário.
@app.route("/api/login", methods=["POST"])
def login():

    # Recebe os dados do frontend.
    dados = request.get_json()
    cpf = dados.get("cpf")
    senha = dados.get("senha")

    # Busca o usuário no banco de dados pelo CPF.
    usuario = Usuario.query.filter_by(cpf=cpf).first()

    # Verifica se o usuário existe e se a senha está correta.
    if not usuario or not check_password_hash(usuario.senha, senha):

        # Login incorreto.
        return jsonify({"erro": "CPF ou senha inválidos..."}), 401

    else:

        # Login correto.
        token = create_access_token(
            identity=str(usuario.id),
            additional_claims={
                "administrador": usuario.administrador
        }
)

        return jsonify({"token": token}), 200


# Rota para logout de usuário.
@app.route("/api/logout", methods=["POST"])
@jwt_required()
def logout():

    return jsonify({"mensagem": "Logout realizado com sucesso!"}), 200

@app.route("/api/usuarios", methods=["POST"])
@jwt_required()
def cadastrar_usuario():
    claims = get_jwt()
    if not claims["administrador"]:
        return jsonify({"erro": "Acesso negado"}), 403
    
    dados = request.get_json()
    nome = dados.get("nome")
    cpf = dados.get("cpf")
    email = dados.get("email")
    senha = dados.get("senha")
    telefone = dados.get("telefone")
    data_nascimento = dados.get("data_nascimentonome")
    administrador = dados.get("administrador", False)
    try:
        if Usuario.query.filter_by(cpf=cpf).first() or Usuario.query.filter_by(email=email).first():
            return jsonify({"error":"CPF ou e-mail já cadastrados..."}), 409
        else:
            novo_usuario = Usuario(
                nome=nome,
                cpf=cpf,
                email=email,
                senha=generate_password_hash(senha),
                telefone=telefone,
                data_nascimento=data_nascimento,
                administrador=administrador
            )
            db.session.add(novo_usuario)
            db.session.commit()
            return jsonify({"mensagem":"Usuário cadastrado com sucesso "})
    except Exception as e:
        # Desfaz as alterações feitas no banco
        db.session.rollback()
        return jsonify({"error": "Não foi cadastrar o usuário..."}), 500
    
@app.route("/api/usuarios", methods=["GET"])
@jwt_required()
def listar_usuarios():
    claims = get_jwt()
    if not claims["administrador"]:
        return jsonify({"erro": "Acesso negado"}), 403
    
    try:
        usuarios = Usuario.query.all()
        resultado = [{
            "id":usuario.id,
            "nome": usuario.nome,
            "cpf":usuario.cpf,
            "email": usuario.email,
            "telefone":usuario.telefone,    
            "administrador":usuario.administrador
        } for usuario in usuarios]
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error":"Não foi possível listar os usuários"})
# Executa a aplicação da web com depuração ativa.

@app.route("/api/tarefa", methods=["POST"])
def registrar_tarefa():
    data = request.get_json()
    titulo = data.get("titulo")
    descricao = data.get("descricao")
    arquivo = data.get("arquivo")
    if Usuario.query.filter_by(titulo=titulo) or Usuario.query.filter_by(descricao=descricao):
        return jsonify({"error":"Tarefa já registrada"})
    
    

if __name__ == "__main__":

    app.run(debug=True)