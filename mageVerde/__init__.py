from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mageverde.db'
app.config['SECRET_KEY'] = 'd679ee02248df5a0448ff4e4a67715cb'

database = SQLAlchemy(app)
Bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'loginUsuario'

from mageVerde import routes