from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mageverde.db'
# lembrar de antes de subir 'secret_key' para o github, criar .gitignore
# e adicionar o arquivo .env com a variável SECRET_KEY
# substituir a linha da chave secreta por: 
# import os
# from dotenv import load_dotenv
# load_dotenv()
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SECRET_KEY'] = 'd679ee02248df5a0448ff4e4a67715cb'

database = SQLAlchemy(app)
Bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'loginUsuario'

from mageVerde import routes