from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, PasswordField, DateField, TimeField
from wtforms.validators import InputRequired, NumberRange, Email, Length, EqualTo
import datetime

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


class ScheduleForm(FlaskForm):

    name = StringField('Nome', validators=[InputRequired()])

    procedure_name = StringField('Procedimento', validators=[InputRequired()])

    date = DateField('Dia', validators=[InputRequired(),
                                         NumberRange(min=10, message=f"Por favor, informe uma data do {datetime.date.today()} em diante.")])
    time = TimeField('Horário', validators=[InputRequired(),
                                            NumberRange(min=8,
                                                        max=18,
                                                        message='Por favor, informe um horário entre 08:00 - 17:00')])
    submit = SubmitField('Agendar')


