from Factory.factory import Transporte

class Caminhao(Transporte):
    def __init__(self, nome):
        self.nome = nome
        self.categoria = 'Caminhão'
        
    def delivery(self):
        return f'{self.categoria} preparado para entrega: {self.nome}, Transporte térreo...'
