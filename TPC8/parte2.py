def contaString (s, subs):
    s.split(subs)
    contador = len(s.split(subs)) - 1
    return contador

def multiplicaMenor (lista):
    lista = sorted(lista)
    print(lista)
    multiplicacao = lista[0] *lista[1]*lista[2]
    return multiplicacao

def addDigits(number):
    if number < 10:
        return number
    else:
        return addDigits(number % 10 + number // 10)


def myIndexOf(s1, s2):
    indice = -1
    i = 0
    while i<len(s1):
        if s1[i:(i+len(s2))] == s2:
            indice = i
        i = i +1
    return indice

