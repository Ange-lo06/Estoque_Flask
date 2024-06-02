from App import db

class Estoque(db.Model):
    __tablename__ = "Estoque"

    id_produto = db.Column(db.Interger, primary_key=True)
    nome_produto = db.Column(db. String, unique=True)
    qtd_produto = db.Column(db.Interger)
    valor_unidade_produto = db.Column(db.Float)


def __init__(self, nome_produto, qtd_produto, valor_unidade_produto):
    self.nome_produto = nome_produto
    self.qtd_produto = qtd_produto
    self.valor_unidade_produto = valor_unidade_produto


#Estoque("Feijão", 300, 3.50)

