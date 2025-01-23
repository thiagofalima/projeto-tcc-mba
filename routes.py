from flask import Blueprint, render_template, request, session, flash, redirect, url_for, current_app
from passlib.hash import pbkdf2_sha256
import uuid
from forms import RegisterForm, LoginForm
from models import Cliente, Agendamento
import datetime

pages = Blueprint('pages', __name__, 
                  template_folder='templates',
                  static_folder='static')

@pages.route('/')
def home():
    return render_template('home.html', title='Jacqueline Agostini')

users = {

}

@pages.route('/register', methods=['GET', 'POST'])
def register():

    if session.get('email'):
        return redirect(url_for('pages.home'))

    form = RegisterForm()

    if form.validate_on_submit():
        cliente = Cliente(
            _id=uuid.uuid4().hex,
            email=form.email.data,
            password=pbkdf2_sha256.hash(form.password.data),
            date=datetime.datetime.now()
        )

        # DB insertion here

        flash('Carastro realizado comn sucesso!', 'success')
        return redirect(url_for('pages.login'))

    return render_template('register.html',
                            title='Jacqueline Agostini - Registrar',
                                form=form )

@pages.route('/login', methods=['GET', 'POST'])
def login():

    if session.get('email'):
        return redirect(url_for('pages.home'))
    
    form = LoginForm()

    if form.validate_on_submit():
        # DB verification
        cliente_data = {}
        if not cliente_data:
            flash('Usuário ou senha incorretos!', 'danger')
            return redirect(url_for('pages.login'))

        cliente = Cliente(**cliente_data)

        if cliente and pbkdf2_sha256.verify(form.password.data, cliente.password):
            session['cliente_id'] = cliente._id
            session['email'] = cliente.email

            return redirect(url_for('pages.home'))
        flash('Usuário ou senha incorretos!', 'danger')

    return render_template('login.html', title='Jacqueline Agostini - Login',
                           form=form)

procedimentos_beleza = {
    'Design de Sobrancelhas': '',
    'Brow Lamination': '',
    'Lash Lifting': ''

}

@pages.route('/beleza')
def beleza():
    return render_template('beleza.html', title='Jacqueline Agostini - Beleza',
                           procedimentos_beleza=procedimentos_beleza)



procedimentos_estetica = {
    'Depilação a Laser': '', 
    'Limpeza de Pele': '', 
    'Microagulhamento': ''}

@pages.route('/estetica')
def estetica():
    return render_template('estetica.html', title='Jacqueline Agostini - Estética',
                           procedimentos_estetica=procedimentos_estetica)

procedimentos_em_estar = {
    'Drenagem Linfática': '',
    'Massagem Relaxante': '',
    'Reflexologia': ''
}

@pages.route('/bem-estar')
def bem_estar():
    return render_template('bem_estar.html', title='Jacqueline Agostini - Bem-estar',
                           procedimentos_em_estar=procedimentos_em_estar)

@pages.route('/agendamento')
def pedido():

    if request.method == 'POST':
        pass

    return render_template('agendamento.html', title='Jacqueline Agostini - Agendamento')