from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, NumberRange, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    
    name = StringField('Nome', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])

    password = PasswordField('Senha', validators=[InputRequired(),
                                                     Length(min=4, message='Sua senha deve ter no mínimo 4 caracteres')])
    
    confirm_password = PasswordField('Senha', validators=[InputRequired(),
                                                          EqualTo('password',
                                                                  message='A senha digitda deve ser igual a senha digitada acima.')])
    
    submit = SubmitField('Cadastrar')

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Senha', validators=[InputRequired()])
    submit = SubmitField('Entrar')