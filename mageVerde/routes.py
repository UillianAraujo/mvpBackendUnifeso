from mageVerde import app, database, Bcrypt
from flask import render_template, redirect, request, url_for
from flask_login import login_required, logout_user, login_user, current_user
from mageVerde.forms import LoginUsuarioForm, LoginAdmForm, CadastroForm, AreaAdmForm, AgendarTrilhasForm
from mageVerde.models import Usuario


@app.route('/')
def inicio():
    return render_template('inicio.html')


#rota do cadastroUsuario
@app.route('/cadastroUsuario', methods=['GET', 'POST'])
def cadastroUsuario():
    form = CadastroForm()
    if form.validate_on_submit():
        senha= Bcrypt.generate_password_hash(form.senha.data) #criptografia da senha
        usuario=Usuario(
            email=form.email.data,
            username=form.username.data,
            senha=senha)
        database.session.add(usuario)
        database.session.commit()
        return redirect(url_for('trilhasUsuario', usuario=usuario.username))  #redireciona para o perfil do usuário após o cadastro
    return render_template('cadastroUsuario.html', form=CadastroForm())


#rota do longinUsuario
@app.route('/loginUsuario', methods=['GET', 'POST'])
def loginUsuario():
    form= LoginUsuarioForm()
    if form.validate_on_submit(): # validade_on_submit() verifica se o formulário foi enviado e se os dados são válidos
        usuario = Usuario.query.filter_by(email=form.email.data).first()  #busca o usuário pelo email
        if usuario and Bcrypt.check_password_hash(usuario.senha, form.senha.data):  # Verifica se a senha está correta
            login_user(usuario)
            return redirect(url_for('perfil', usuario=usuario))  #redireciona para a página de trilhas do usuário
    return render_template('loginUsuario.html', form=LoginUsuarioForm())
    


#rota do longinAdm
@app.route('/loginAdm', methods=['GET', 'POST'])
def loginAdm():
    form= LoginAdmForm()
    return render_template('loginAdm.html', form=LoginAdmForm())


#@app.route('/trilhasUsuario', methods=['GET'])
#def trilhasUsuario():
#    return render_template('trilhasUsuario.html')


#rota da areaAdm
@app.route('/areaAdm', methods=['GET'])
def areaAdm():
    return render_template('areaAdm.html')


#rota dinâmica perfilUsuario
@app.route('/trilhasUsuario/<usuario>', methods=['GET', 'POST'])
@login_required
def perfil(usuario):
    form = AgendarTrilhasForm()
    mensagem = None

    if form.validate_on_submit():
        # Aqui você pode adicionar a lógica para agendar trilhas
        # Por exemplo, salvar a trilha agendada no banco de dados
        mensagem = "Trilha agendada com sucesso!"
    
    return render_template('trilhasUsuario.html', usuario=usuario, form=form, mensagem=mensagem)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('loginUsuario'))

#@app.route('/trilhasUsuario', methods=['GET', 'POST'])
#@login_required
#def agendarTrilhas():
#    form= AgendarTrilhasForm()
#    return render_template('trilhasUsuario.html', form=AgendarTrilhasForm())