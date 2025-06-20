from mageVerde import app
from flask import render_template, redirect, request, url_for
from flask_login import login_required
from mageVerde.forms import LoginUsuarioForm, LoginAdmForm, CadastroForm, AreaAdmForm

@app.route('/')
def inicio():
    return render_template('inicio.html')

#rota do longinUsuario
@app.route('/loginUsuario', methods=['GET', 'POST'])
def loginUsuario():
    return render_template('loginUsuario.html', form=LoginUsuarioForm())

#rota do longinAdm
@app.route('/loginAdm', methods=['GET', 'POST'])
def loginAdm():
    return render_template('loginAdm.html')

#rota da areaAdm
@app.route('/areaAdm', methods=['GET'])
def areaAdm():
    return render_template('areaAdm.html')

#rota dinâmica perfilUsuario
@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('perfil.html, usuario=usuario)')