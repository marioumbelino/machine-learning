# Questão 01

from random import randint

def impar(lista):
    impares = []
    for numero in lista:
        if numero % 2 == 1:
            impares.append(numero)
    return impares

teste = [randint(0, 100) for i in range(10)]

print(teste)

impares = impar(teste)

print(impares)
