from Factory import Factory
from Transportes import Navio

class LogisticaMaritima(Factory):
    def __init__(self, nome):
        self.nome = nome

    def criar_transporte(self):
        return Navio(self.nome)
