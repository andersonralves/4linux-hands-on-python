from flask import Blueprint
import click
import json
import pandas as pd
from ..extensions.database import mongo

productCommands = Blueprint('product', __name__)


@productCommands.cli.command("import")
@click.argument("csvfile")
def import_csv(csvfile: str):
    
    data = pd.read_csv(csvfile)
    jsondata = json.loads(data.to_json(orient="records"))

    collection = mongo.db.produtos
    qtde_registros = collection.estimated_document_count()    
    
    collection.insert(jsondata)

    qtde_atual = collection.estimated_document_count()
    qtde_inserida = qtde_atual - qtde_registros
    
    print(f'{qtde_inserida} registros inseridos')
    return
    