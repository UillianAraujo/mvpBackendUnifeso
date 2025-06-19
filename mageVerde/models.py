# criar a estrutura do banco de dados

from mageVerde import database, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), nullable=False)
    email = database.Column(database.String(50), unique=True, nullable=False)
    senha = database.Column(database.String(20), nullable=False)

class Adm(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), nullable=False)
    email = database.Column(database.String(50), unique=True, nullable=False)
    matricula = database.Column(database.Integer, unique=True, nullable=False)
    senha = database.Column(database.String(20), nullable=False)