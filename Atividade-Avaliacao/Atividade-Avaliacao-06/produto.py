from flaskp import db

class Produto(db.Model):
    __tablename__ = "TB_PRODUTO"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String, unique=True)
    descricao = db.Column(db.String)
    valorUnitario = db.Column(db.Float)

    def __init__(self, id, codigo, descricao, valorUnitario):
        self._id = id
        self._codigo = codigo
        self._descricao = descricao
        self._valorUnitario = valorUnitario

    def getDescricao(self):
        return self._descricao

    def getValorUnitario(self):
        return self._valorUnitario

    def str(self):
        string = "\nId={3} Codigo={2} Descricao={1} Valor Unitario={0}".format(self._valorUnitario, self._descricao,
                                                                               self._codigo, self._id)
        return string


if __name__ == '__main__':
    produto = Produto(1, 100, 'Arroz', 5.5)
    print(produto.str())