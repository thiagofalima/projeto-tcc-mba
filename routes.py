from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from passlib.hash import pbkdf2_sha256

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

    if request.method == "POST":
        user = session["user"]
        password = pbkdf2_sha256(session["password"])
        users[user] = password
        flash("Cadastro realizado com sucesso!")
        print(users)

        return redirect(url_for('pages.home'))


    return render_template('register.html', title='Jacqueline Agostini - Registrar' )

@pages.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        pass

    return render_template('login.html', title='Jacqueline Agostini - Login')

procedimentos_beleza = {

}

@pages.route('/beleza')
def beleza():
    return render_template('beleza.html', title='Jacqueline Agostini - Beleza',
                           procedimentos_beleza=procedimentos_beleza)

procedimentos_estetica = {

}

@pages.route('/estetica')
def estetica():
    return render_template('estetica.html', title='Jacqueline Agostini - Estética',
                           procedimentos_estetica=procedimentos_estetica)

procedimentos_em_estar = {

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