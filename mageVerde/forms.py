# criar os formularios do site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField, TimeField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from mageVerde.models import Usuario

class LoginUsuarioForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=20)])
    botaoConfirmacao = SubmitField('Fazer Login')

class LoginAdmForm(FlaskForm):
    matricula = StringField('Nº Matrícula', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=20)])
    botaoConfirmacao = SubmitField('Fazer Login')

# não pretendo criar um template/formulário para cadastrar usuários.
class CadastroForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Nome', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=20)])
    confirmarSenha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    botaoConfirmacao = SubmitField('Cadastrar')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError('E-mail já cadastrado, faça login.')

# form adcionar trilhas disponíveis
class AreaAdmForm():
    pass

class AgendarTrilhasForm(FlaskForm):
    trilha = SelectField('Trilhas', choices=[('1','Parque Nacional da Serra dos Órgãos'), ('2','Parque Municipal Barão de Mauá')],
                          coerce=int, validators=[DataRequired()])
    data = DateField('Data', format='%D/%m/%y', validators=[DataRequired()])
    horario = TimeField('Horário', format='%H', validators=[DataRequired()])
    botaoConfirmacao = SubmitField('Agendar')