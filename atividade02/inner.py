# Questão 3
"""função randint da biblioteca random gera números inteiros aleatórios entre um intervalo."""
from random import randint

def inner_join(lista1, lista2):
    """Retorna uma lista de elementos em comum entre duas listas. Semelhante ao Inner Join em SQL.

    Args:
        lista1 (list): primeira lista de elementos numéricos para comparação
        lista2 (list): segunda lista de elementos numéricos para comparação

    Returns:
        list: lista de elementros em comum entre a lista1 e a lista2
    """
    elementos_comum = []
    for item in lista1:
        if item in lista2:
            elementos_comum.append(item)
    return elementos_comum

# teste
lista_teste1 = [randint(0, 100) for i in range(10)]
lista_teste2 = [randint(0, 100) for i in range(10)]

print(lista_teste1)
print(lista_teste2)

lista_inner = inner_join(lista_teste1, lista_teste2)

print(lista_inner)
