from Tipo_de_Cliente  import Tipo_Cliente

class Cliente():
    def __init__(self, id, nome, codigo, cnpjcpf, tipo):
        self._id = id
        self._nome = nome
        self._codigo = codigo
        self._cnpjcpf = cnpjcpf
        self._tipo = tipo
        
    def str(self):
        string="\nId={4} Codigo={2} Nome={3} CNPJ/CPF={1} Tipo={0}".format(self._tipo,
                                                                           self._cnpjcpf,
                                                                           self._codigo,
                                                                           self._nome,
                                                                           self._id)
        return string
    
if __name__ == '__main__':
    cliente=Cliente(1, "José Simão da Silva", 1234, "200.100.345-34", Tipo_Cliente.PESSOA_FISICA)
    print(cliente.str())