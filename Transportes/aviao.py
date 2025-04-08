from Factory.factory import Transporte

class Aviao(Transporte):
    def __init__(self, nome):
        self.nome = nome
        self.categoria = 'Avião'
        
    def delivery(self):
        return f'{self.categoria} preparado para entrega: {self.nome}, Transporte aéreo...'
