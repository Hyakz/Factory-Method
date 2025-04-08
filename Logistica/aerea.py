from Factory import Factory
from Transportes import Aviao

class LogisticaAerea(Factory):
    def __init__(self, nome):
        self.nome = nome

    def criar_transporte(self):
        return Aviao(self.nome)