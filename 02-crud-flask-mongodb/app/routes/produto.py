from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from ..extensions.database import mongo

produto = Blueprint('produto', __name__)

@produto.route("/list")
def listarProdutos():
    if "username" in session:
        produtos = mongo.db.produtos.find()
        return render_template('produtos/list.html', produtos = produtos)
    else:
        return redirect(url_for('usuario.index'))

@produto.route("/insert", methods=["GET", "POST"])
def inserirProduto():
    if "username" in session:
        if request.method == 'GET':
            produtos = mongo.db.produtos.find()
            return render_template('produtos/insert.html')
        else:
            nome = request.form.get("nome")
            quantidade = request.form.get("quantidade")
            preco = request.form.get("preco")
            categoria = request.form.get("categoria")
            estoque = request.form.get("estoque")

            if not nome or len(nome) > 50:
                flash("Campo é obrigatório e deve ter no máximo 50 caracteres")
            elif not quantidade or not quantidade.isdigit() or int(quantidade) <= 0:
                flash("Informe uma quantidade correta")
            elif not preco:
                flash("Campo 'preço' é obrigatório")
            elif not categoria:
                flash("Campo 'categoria' é obrigatório")
            elif not estoque:
                flash("Campo 'estoque' é obrigatório")
            else:
                mongo.db.produtos.insert_one({
                    "produto": nome,
                    "quantidade": quantidade,
                    "preco": preco,
                    "categoria": categoria,
                    "estoque": estoque,
                    "valor_total": (float(quantidade) * float(preco))
                })

                flash("Produto cadastrado com sucesso!")
                return redirect(url_for("produto.listarProdutos"))

    else:
        return redirect(url_for('usuario.index'))

@produto.route("/edit", methods=["GET", "POST"])
def editarProduto():
    if request.method == "GET":
        idProduto = request.values.get("idproduto")

        if not idProduto:
            flash("Campo 'idproduto' é obrigatório")
        else:
            idProd = mongo.db.produtos.find({"_id": ObjectId(idProduto)})
            produto = [prd for prd in idProd]
            estoques = set()
            produtos = mongo.db.produtos.find()
            for p in produtos:
                estoques.add(p['estoque'])
            return render_template("produtos/edit.html", produto=produto, estoques=estoques)
    else:
        idProduto = request.form.get("idproduto")
        nome = request.form.get("nome")
        quantidade = request.form.get("quantidade")
        preco = request.form.get("preco")
        categoria = request.form.get("categoria")
        estoque = request.form.get("estoque")

        if not idProduto:
            flash("Campo 'idproduto' é obrigatório")
        elif not nome or len(nome) > 50:
            flash("Campo é obrigatório e deve ter no máximo 50 caracteres")
        elif not quantidade or not quantidade.isdigit() or int(quantidade) <= 0:
            flash("Informe uma quantidade correta")
        elif not preco:
            flash("Campo 'preço' é obrigatório")
        elif not categoria:
            flash("Campo 'categoria' é obrigatório")
        elif not estoque:
            flash("Campo 'estoque' é obrigatório")
        else:
            mongo.db.produtos.update({"_id": ObjectId(idProduto)}, {
                "$set": {
                    "produto": nome,
                    "quantidade": quantidade,
                    "preco": preco,
                    "categoria": categoria,
                    "estoque": estoque,
                    "valor_total": (float(quantidade) * float(preco))
                }
            })
            flash("Produto atualizado com sucesso!")
    return redirect(url_for("produto.listarProdutos"))

@produto.route("/delete")
def deletarProduto():

    idProduto = request.values.get("idproduto")

    if not idProduto:
        flash("Campo 'idproduto' é obrigatório")
    else:
        idProd = mongo.db.produtos.find({"_id": ObjectId(idProduto)})

        if not idProd:
            flash("Produto não cadastrado")
        else:
            mongo.db.produtos.delete_one({'_id': ObjectId(idProduto)})
            flash("Produto excluido com sucesso")

    return redirect(url_for("produto.listarProdutos"))