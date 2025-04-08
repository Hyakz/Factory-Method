from Factory import Factory
from Transportes import Caminhao

class LogisticaEstrada(Factory):
    def __init__(self, nome):
        self.nome = nome

    def criar_transporte(self):
        return Caminhao(self.nome)