from abc import ABC, abstractmethod

class Factory(ABC):
    def criar_transporte(self):
        pass

    def planoDelivery(self):
        transporte = self.criar_transporte()
        resultado = f'Logistica: Transporte sendo preparado...\n{transporte.delivery()}'
        return resultado

class Transporte(ABC):
    @abstractmethod
    def delivery(self):
        pass
