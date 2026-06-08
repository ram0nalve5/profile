from database import db
class Usuario (db.Model):
    __tablename__ = "usuario"
    cpf = db.Column(db.String(14), primary_key=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    
    