import random

# computador cria uma lista
def criaLista():
    size = int(input('Escolha o tamanho desejado da lista:'))
    return [random.randint(1,100) for i in range(size)]
   
# utilizar introduz uma lista
def introduzLista():
    lista = []
    size = int(input('Escolha o tamanho desejado da lista:'))
    while size >0 :
        lista.append(int(input('Digite um número para adicionar à lista.')))
        size = size - 1
    return lista

# somar os elementos da lista
def somaLista(lista):
    a = 0
    for c in lista:
        a = a + c
    return a

#calcular a media da lista de numeros
def mediaLista(lista):
    a = 0
    b = 0
    for c in lista:
        a = a + c
        b = b+1
    return a/b

#calcular o maior elemento da lista
def maiorLista( lista):
    res = lista[0]
    for x in lista:
        if x>res:
            res = x
    return res

#calcular o menor numero da lista
def menorLista(lista):
    a = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] < a:
            a = lista[i]
        i = i+1
    return a

#verificar se a lista esta ordenada crescente
def estaOrdenadaC(lista):
    i = 0
    res = True
    while i< len(lista) - 1 and res:
        if lista[i] > lista[i+1]:
            res = False
        else:
            res = True
            i = i +1
    return res

#verificar se a lista esta ordenada decrescente
def estaOrdenadaD(lista):
    i = 0
    res = True
    while i< len(lista) - 1 and res:
        if lista[i] < lista[i+1]:
            res = False
        else:
            res = True
            i = i +1
    return res

#procurar elemento na lista
def procuraEl (lista, elemento):
    res = False
    indice = -1 
    i = 0
    while i < len(lista) and not res:
        if elemento == lista[i]:
            res = True
            indice = i
        else:
            i = i + 1
    return indice

