# Questão 02
from random import randint
from math import sqrt

def primos(lista):
    """Verifica, em uma lista, quais números são primos e retorna-os em uma lista.

    Args:
        lista (list): lista de números a serem verificados.

    Returns:
        list: números primos contidos na lista passada inicialmente. 
    """
    lista_primos = []
    for numero in lista:
        if numero < 2:
            continue
        e_primo = True
        for divisor in range(2, round(sqrt(numero) + 1)):
            if numero % divisor == 0:
                e_primo = False
                break
        if e_primo:
            lista_primos.append(numero)
    return lista_primos

teste = [randint(0, 100) for i in range(10)]

print(teste)

primos_teste = primos(teste)

print(primos_teste)
