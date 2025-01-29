from flask import (
    Blueprint,
    render_template,
    request,
    session,
    flash,
    redirect,
    url_for,
    current_app,
)
from passlib.hash import pbkdf2_sha256
import uuid
from forms import RegisterForm, LoginForm, ScheduleForm
from models import Cliente, Agendamento, Procedimento
import datetime
from dataclasses import asdict

pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)

queridinhos = {
    "Limpeza de Pele": "A Limpeza de Pele é um procedimento fundamental para manter a saúde e beleza da pele, removendo impurezas, células mortas e cravos, através da aplicação de produtos específicos e técnicas de extração.",
    "Depilação a Laser": """A Depilação a Laser é um método de depilação duradoura que utiliza a tecnologia do laser para eliminar os pelos desde a raiz, proporcionando resultados eficazes e de longa duração, através da emissão de luz que é absorvida pela melanina do pelo.""",
    "Drenagem Linfática": "A Drenagem Linfática é uma técnica de massagem que estimula o sistema linfático, responsável pela eliminação de toxinas e 1  líquidos retidos no corpo, proporcionando diversos benefícios para a saúde e bem-estar.",
}


@pages.route("/", methods=["GET"])
def home():

    return render_template(
        "home.html", title="Jacqueline Agostini", queridinhos=queridinhos
    )


@pages.route("/register", methods=["GET", "POST"])
def register():

    if session.get("email"):
        return redirect(url_for(".home"))

    form = RegisterForm()

    if form.validate_on_submit():
        cliente = Cliente(
            _id=uuid.uuid4().hex,
            name=form.name.data,
            email=form.email.data,
            password=pbkdf2_sha256.hash(form.password.data),
            register_date=datetime.datetime.now().isoformat(),
        )

        current_app.db.clientes.insert_one(asdict(cliente))

        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for("pages.login"))

    return render_template(
        "register.html", title="Jacqueline Agostini - Registrar", form=form
    )


@pages.route("/login", methods=["GET", "POST"])
def login():

    if session.get("email"):
        return redirect(url_for(".home"))

    form = LoginForm()

    if form.validate_on_submit():
        # DB verification
        cliente_data = current_app.db.clientes.find_one({"email": form.email.data})
        if not cliente_data:
            flash("Usuário ou senha incorretos!", "danger")
            return redirect(url_for("pages.login"))
        cliente = Cliente(**cliente_data)

        if cliente and pbkdf2_sha256.verify(form.password.data, cliente.password):
            session["cliente_id"] = cliente._id
            session["email"] = cliente.email

            return redirect(url_for("pages.home"))
        flash("Usuário ou senha incorretos!", "danger")

    return render_template("login.html", title="Jacqueline Agostini - Login", form=form)


procedimentos_beleza = {
    "Design de Sobrancelhas": """O design de sobrancelhas é um serviço personalizado que visa realçar a beleza natural do rosto, moldando as sobrancelhas de forma harmoniosa e individualizada, 
levando em consideração as características faciais de cada pessoa e utilizando técnicas como pinça, linha e henna.
""",
    "Brow Lamination": """O Brow Lamination é uma técnica inovadora que alinha os fios das sobrancelhas, proporcionando um aspecto mais volumoso, uniforme e natural, através da aplicação de produtos específicos que modelam e fixam os fios""",
    "Lash Lifting": """O Lash Lifting é um procedimento que curva e levanta os cílios desde a raiz, proporcionando um olhar mais expressivo e realçado, sem a necessidade de cílios postiços, através da aplicação de produtos e técnicas específicas.""",
}


@pages.route("/beleza")
def beleza():
    return render_template(
        "beleza.html",
        title="Jacqueline Agostini - Beleza",
        procedimentos_beleza=procedimentos_beleza,
    )


procedimentos_estetica = {
    "Depilação a Laser": """A Depilação a Laser é um método de depilação duradoura que utiliza a tecnologia do laser para eliminar os pelos desde a raiz, proporcionando resultados eficazes e de longa duração, através da emissão de luz que é absorvida pela melanina do pelo.""",
    "Limpeza de Pele": "A Limpeza de Pele é um procedimento fundamental para manter a saúde e beleza da pele, removendo impurezas, células mortas e cravos, através da aplicação de produtos específicos e técnicas de extração.",
    "Microagulhamento": "O Microagulhamento é uma técnica que utiliza um aparelho com microagulhas para estimular a produção de colágeno e elastina na pele, promovendo a renovação celular e o tratamento de diversas condições, como rugas, cicatrizes de acne e manchas.",
}


@pages.route("/estetica")
def estetica():
    return render_template(
        "estetica.html",
        title="Jacqueline Agostini - Estética",
        procedimentos_estetica=procedimentos_estetica,
    )


procedimentos_em_estar = {
    "Drenagem Linfática": "A Drenagem Linfática é uma técnica de massagem que estimula o sistema linfático, responsável pela eliminação de toxinas e 1  líquidos retidos no corpo, proporcionando diversos benefícios para a saúde e bem-estar.",
    "Massagem Relaxante": "A Massagem Relaxante é uma técnica que utiliza movimentos suaves e relaxantes para aliviar tensões musculares, promover o relaxamento do corpo e da mente, e proporcionar bem-estar geral.",
    "Reflexologia": "A Reflexologia é uma técnica milenar que utiliza a pressão em pontos específicos dos pés para promover o equilíbrio energético do corpo e tratar diversas condições de saúde.",
}


@pages.route("/bem-estar")
def bem_estar():
    return render_template(
        "bem_estar.html",
        title="Jacqueline Agostini - Bem-estar",
        procedimentos_em_estar=procedimentos_em_estar,
    )


@pages.route("/agendamento", methods=["GET", "POST"])
def agendamento():

    form = ScheduleForm()

    if form.is_submitted():

        agendamento = Agendamento(
            _id=uuid.uuid4().hex,
            cliente=form.name.data,
            procedimento=form.procedure_name.data,
            date=form.date.data,
            time=form.time.data,
        )

        agendamento.convert_date()
        agendamento.convert_time()

        current_app.db.agendamentos.insert_one(asdict(agendamento))

        # print(type(form.date.data))
        # print(type(form.time.data))

        flash(f"Agendamento feito com sucesso!", "success")
        flash(
            f"{agendamento.procedimento} para o dia {agendamento.date} às {agendamento.time}",
            "success",
        )

    return render_template(
        "agendamento.html", title="Jacqueline Agostini - Agendamento", form=form
    )


@pages.route("/logout")
def logout():
    session.clear()

    return redirect(url_for(".login"))
