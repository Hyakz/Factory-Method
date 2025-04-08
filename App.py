from Logistica import LogisticaEstrada, LogisticaMaritima, LogisticaAerea
from Factory   import Factory

def executarEntrega(logistica: Factory):
    print(f'App: Carregado com {logistica.__class__.__name__}.\n{logistica.planoDelivery()}')

if __name__ == '__main__':
    executarEntrega(LogisticaEstrada('Caminhão - 01'))
    
    print('') # Espaço entre as linhas
    
    executarEntrega(LogisticaMaritima('Navio - 01'))
    
    print('') # Espaço entre as linhas
    
    executarEntrega(LogisticaAerea('Avião - 01'))