from mageVerde import app
from flask import render_template, redirect, request, url_for


@app.route('/')
def inicio():
    return render_template('inicio.html')

#rota do longinUsuario
@app.route('/loginUsuario', methods=['GET'])
def loginUsuario():
    return render_template('loginUsuario.html')

#rota do longinAdm
@app.route('/loginAdm', methods=['GET'])
def loginAdm():
    return render_template('loginAdm.html')

#rota da areaAdm
@app.route('/areaAdm', methods=['GET'])
def areaAdm():
    return render_template('areaAdm.html')

#rota dinâmica perfilUsuario
@app.route('/perfil/<usuario>')
def perfil():
    return render_template('perfil.html')