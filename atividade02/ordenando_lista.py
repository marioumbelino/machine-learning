# Questão 05

def ordenar_usuarios(lista):
    """Função recebe uma lista de tuplas e retorna a lista ordenada por ordem alfabética (ou númerica, a depender do conteúdo da tupla).

    Args:
        lista (list): lista de tuplas com nome e idade a serem ordenados.

    Returns:
        list: retorna a lista ordenada
    """
    for tupla in range(len(lista)): # percorre por toda a lista, escolhendo a primeira tupla a ser comparada
        for tupla_seguinte in range(tupla + 1, len(lista)): # percorre toda a lista, escolhendo a segunda tupla a ser comparada com a primeira
            if lista[tupla][0] > lista[tupla_seguinte][0]: 
                lista[tupla], lista[tupla_seguinte] = lista[tupla_seguinte], lista[tupla] # realiza a ordenação da lista
    return lista


# Teste
lista_teste = [('Mário', 19), ('Talita', 19), ('Leila', 25), ('Erick', 31), ('Elon', 52), ('Alexandre', 55)]

lista_ordenada = ordenar_usuarios(lista_teste)

print(lista_ordenada)