from Factory import Transporte

class Navio(Transporte):
    def __init__(self, nome):
        self.nome = nome
        self.categoria = 'Navio'
        
    def delivery(self):
        return f'{self.categoria} preparado para entrega: {self.nome}, Transporte marítimo...'
