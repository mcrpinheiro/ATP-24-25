def naoComum (lista1, lista2):
    novalista = []
    for num in lista1:
        if num not in lista2:
            novalista.append(num)
    for nums in lista2:
        if nums not in lista1:
            novalista.append(nums)
    return novalista

def palsLongas (texto):
    palavras = texto.split(' ')
    palavrasLonga = []
    for pal in palavras:
        if len(pal)>3:
            palavrasLonga.append(pal)
    return palavrasLonga

def indiceValor (lista):
    i = 1
    listaIndices =[]
    for valor in lista:
        listaIndices.append((i, valor))
        i = i +1
    return listaIndices

