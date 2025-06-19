# criar a estrutura do banco de dados

from mageVerde import database

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