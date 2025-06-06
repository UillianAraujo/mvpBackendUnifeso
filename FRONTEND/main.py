from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MVPUILLIAuiNARAUJO'
@app.route('/')
def inicio():
    return render_template('inicio.html')

#rota do longinUsuário

@app.route('/loginUsuario', methods=['POST'])
def longinUsuario():
    nome = request.form.get('username')
    senha = request.form.get('password')


    return redirect('/loginUsuario')

#rota do longinAdmin

@app.route('/loginAdmin', methods=['POST'])
def longinAdmin():
    nome = request.form.get('username')
    senha = request.form.get('password')

    return redirect('/loginAdmin')



if __name__ == '__main__':
    app.run(debug=True)