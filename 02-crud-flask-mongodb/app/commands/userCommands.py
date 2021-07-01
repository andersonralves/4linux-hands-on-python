import click
import getpass
from ..extensions.database import mongo
from werkzeug.security import generate_password_hash
from flask import Blueprint
from validate_email import validate_email

userCommands = Blueprint('user', __name__)

@userCommands.cli.command("getUserByEmail")
@click.argument("email")
def getUser(email: str):
    userCollection = mongo.db.users
    user = [u for u in userCollection.find({"email": email}, {"password": 0})]

    if not user:
        print("Usuario não encontrado")
        return

    print(user)

@userCommands.cli.command("addUser")
def createUser():
    userCollection = mongo.db.users

    name = input("Digite seu nome: ")
    if not name.strip():
        print("Nome não pode ser vazio")
        return

    email = input("Digite seu email: ")
    if not validate_email(email):
        print("Email inválido")
        return

    password = getpass.getpass()
    user = {
        "name": name,
        "email": email,
        "password": generate_password_hash(password)
    }

    userExists = userCollection.find_one({"name": name})
    if userExists:
        print(f'Usuario {name} já existe')
        return

    newUser = userCollection.insert(user)
    if not newUser:
        print('Não foi possível cadastrar o usuário')
        return

    print('Usuário cadastrado com sucesso!')

@userCommands.cli.command("dropUser")
@click.argument("email")
def delete_user(email):
    userCollection = mongo.db.users

    userExists = userCollection.find_one({"email": email})
    if userExists:
        question = input(f'Deseja realmente deletar o usuário {email}? (S/N): ')
        if question.upper() == "S":
           userCollection.delete_one({email: email})
           print("Usuário excluido com sucesso")
        else:
            exit()
    else:
        print("Usuário não encontrado")