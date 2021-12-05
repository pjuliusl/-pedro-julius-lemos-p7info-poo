from produto import Produto
from flaskp import db


class ItemNotaFiscal(db.Model):
    __tablename__ = "TB_ITEM_NOTA_FISCAL"
    id = db.Column(db.Integer, primary_key=True)
    id_notafiscal = db.Column(db.Integer, db.ForeignKey("TB_NOTA_FISCAL.id"))
    sequencial = db.Column(db.String)
    quantidade = db.Column(db.Integer)
    produto = db.Column(db.String, db.ForeignKey("TB_PRODUTO.codigo"))
    descricao = db.Column(db.String, db.ForeignKey("TB_PRODUTO.descricao"))
    valorUnitario = db.Column(db.Float, db.ForeignKey("TB_PRODUTO.valorUnitario"))
    valorItem = db.Column(db.Float)

    nota_fiscal = db.relationship("NotaFiscal", foreign_keys=id_notafiscal)
    produto = db.relationship("Produto", foreign_keys=produto)
    descricao = db.relationship("Produto", foreign_keys=descricao)
    valor_unitario = db.relationship("Produto", foreign_keys=valorUnitario)

    def __init__(self, id, sequencial, quantidade, produto):
        self._id = id
        self._sequencial = sequencial
        self._quantidade = quantidade
        self._produto = produto
        self._descricao = self._produto.getDescricao()
        self._valorUnitario = self._produto.getValorUnitario()
        self._valorItem = float(self._quantidade * self._valorUnitario)

    def str(self):
        string = "\nId={5} Sequencial={4} Quantidade={3} Produto={2} Valor Unitario={1} Valor Item={0}".format(
            self._valorItem,
            self._valorUnitario,
            self._descricao,
            self._quantidade,
            self._sequencial,
            self._id)
        return string

    def getId(self):
        return self._id

    def getvalorItem(self):
        return self._valorItem

    def getValorUnitario(self):
        return self._valorUnitario

    def getDescricao(self):
        return self._descricao

    def getQuantidade(self):
        return self._quantidade

    def getSequencial(self):
        return self._sequencial

if __name__ == '__main__':
    produto = Produto(1, 100, 'Arroz', 5.5)
    item = ItemNotaFiscal(1, 1, 12, produto)
    print(item.str())