# Questão 04
"""função randint da biblioteca random gera números inteiros aleatórios entre um intervalo."""
from random import randint


def segundo_maior(lista):
    """Verifica qual é um maior número dentro de uma lista de números

    Args:
        lista (list): lista de elementos a ser verificado

    Returns:
        int: segundo maior elemento dentro da lista
    """
    lista = set(lista)
    lista.remove(max(lista))
    for numero in lista:
        if numero == max(lista):
            return numero

# teste
lista_teste = [randint(0, 100) for i in range(10)]

print(lista_teste)

print(f"O segundo maior número presente na lista indicada é o {segundo_maior(lista_teste)}")
