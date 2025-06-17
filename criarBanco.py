from mageVerde import database, app
from mageVerde.models import Usuario

with app.app_context():
    database.create_all()