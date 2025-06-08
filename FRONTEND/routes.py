from main import app
from flask import render_template, redirect, request


@app.route('/')
def inicio():
    return render_template('inicio.html')

#rota do longinUsuário

@app.route('/loginUsuario', methods=['POST'])
def loginUsuario():
    nome = request.form.get('username')
    senha = request.form.get('password')

    return redirect('/loginUsuario')

#rota do longinAdmin

@app.route('/loginAdm', methods=['POST'])
def loginAdm():
    nome = request.form.get('username')
    senha = request.form.get('password')

    return redirect('/loginAdm')