from Flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'UILLIANARAUJO'


@app.route('/')
def home():
    return render_template('inicio.html')

#Rota do loginUsuario

@app.route('/loginUsuario', methods=['POST'])
def loginUsuario():

    nome = request.form.get('username')
    senha = request.form.get('password')

    print(nome, senha)
    return redirect('/loginUsuario')

#Rota do loginAdmin






if __name__ == '__main__':
    app.run(debug=True)