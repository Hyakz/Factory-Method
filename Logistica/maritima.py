from Factory.factory import Factory
from Transportes.navio import Navio

class LogisticaMaritima(Factory):
    def __init__(self, nome):
        self.nome = nome

    def criar_transporte(self):
        return Navio(self.nome)
