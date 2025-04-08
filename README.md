# 🏭 Factory Method - Exemplo com Logística

Este projeto demonstra a aplicação do padrão de projeto **Factory Method** utilizando o contexto de diferentes meios de transporte logístico. A implementação foi feita em **Python** com foco em legibilidade, manutenção e boas práticas;

## 🎯 Objetivo

Aplicar o padrão **Factory Method** para encapsular a criação de objetos relacionados a transportes logísticos (avião, caminhão, navio), permitindo flexibilidade e fácil extensão para novos tipos de transporte.

## 🧱 Estrutura do Projeto

```text
FactoryMethod/
├── App.py
├── Factory/
│   └── factory.py
├── Logistica/
│   ├── aerea.py
│   ├── terrestre.py
│   └── maritima.py
└── Transportes/
    ├── aviao.py
    ├── caminhao.py
    └── navio.py
```

### Neste projeto:

- A **Factory** (`factory.py`) define o método `criar_transporte()`.
- As **Logistica** (`aerea.py`, `terrestre.py`, `maritima.py`) implementam esse método, retornando instâncias dos transportes correspondentes.
- Os **Transportes** (`aviao.py`, `caminhao.py`, `navio.py`) contêm a lógica específica de cada tipo.
