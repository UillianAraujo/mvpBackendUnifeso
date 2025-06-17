# Na main: importar o FLASK
# Criar as bases do site
# Criar sistemas de autenticação
# Criar banco de dados
# ...

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MVPUILLIANARAUJO'

from routes import *



if __name__ == '__main__':
    app.run(debug=True)