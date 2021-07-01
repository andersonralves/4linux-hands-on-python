from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from ..extensions.database import mongo
from werkzeug.security import check_password_hash

usuario = Blueprint('usuario', __name__)

@usuario.route('/')
def index():
    return redirect(url_for("usuario.login"))

@usuario.route('/home')
def home():
    if session["username"]:
        return render_template("usuarios/main.html")
    else:
        return redirect(url_for("usuario.index"))

@usuario.route("/login", methods=['GET', 'POST'])
def login():
    if "username" in session:
        return redirect(url_for("usuario.home"))
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('senha')

        userFound = mongo.db.users.find_one({"email": email})
        if userFound:
            validUser = userFound["email"]
            validPassword = userFound["password"]
            if check_password_hash(validPassword, password):
                session["username"] = validUser
                return redirect(url_for('usuario.home'))
            else:
                flash('Senha Incorreta')
        else:
            flash('Usuário não encontrado')

    return render_template("usuarios/login.html")

@usuario.route("/logout")
def logout():
    session.pop("username", None)
    flash("Logout Efetuado!")
    return redirect(url_for("usuario.login"))