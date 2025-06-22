from mageVerde import app, database, Bcrypt
from flask import render_template, redirect, request, url_for
from flask_login import login_required, logout_user, login_user
from mageVerde.forms import LoginUsuarioForm, LoginAdmForm, CadastroForm, AreaAdmForm
from mageVerde.models import Usuario

@app.route('/')
def inicio():
    return render_template('inicio.html')

#rota do cadastroUsuario
@app.route('/cadastroUsuario', methods=['GET', 'POST'])
def cadastroUsuario():
    form = CadastroForm()
    if form.validate_on_submit():
        senha= Bcrypt.generate_password_hash(form.senha.data) # Criptografia da senha
        usuario= Usuario(
            email=form.email.data,
            username=form.username.data,
            senha=senha)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)  # Faz o login do usuário após o cadastro
        return redirect(url_for('perfil', usuario=usuario.username))  # Redireciona para o perfil do usuário após o cadastro
    return render_template('cadastroUsuario.html', form=CadastroForm())

#rota do longinUsuario
@app.route('/loginUsuario', methods=['GET', 'POST'])
def loginUsuario():
    form= LoginUsuarioForm()
    if form.validate_on_submit(): # validade_on_submit() verifica se o formulário foi enviado e se os dados são válidos

        return redirect(url_for('inicio'))
    return render_template('loginUsuario.html', form=LoginUsuarioForm())

#rota do longinAdm
@app.route('/loginAdm', methods=['GET', 'POST'])
def loginAdm():
    form= LoginAdmForm()
    return render_template('loginAdm.html', form=LoginAdmForm())

#rota da areaAdm
@app.route('/areaAdm', methods=['GET'])
def areaAdm():
    return render_template('areaAdm.html')

#rota dinâmica perfilUsuario
@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('trilhasUsuario.html', usuario=usuario)