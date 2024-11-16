import matplotlib.pyplot

def carregaTabMeteo(fnome):
    res = []
    
    f = open(fnome, "r")
    for linha in f:
        data = linha.split("::")
        res.append(((int(data[0]), int(data[1]), int(data[2])), float(data[3]), float(data[4]), float(data[5])))
    
    
    f.close()
    return res


def medias(tabMeteo):
    res = []
    i = 0
    while i < len(tabMeteo):
        res.append((tabMeteo[i][0], (tabMeteo[i][1] + tabMeteo[i][2])/2))
        i = i+1
    return res

def minTemp(tabMeteo):
    i = 1
    minima = tabMeteo[0][1]
    while i < len(tabMeteo) -1:
        if tabMeteo[i][1] < minima:
            minima = tabMeteo[i][1]
        i = i +1
    return minima

def amplTerm(tabMeteo):
    res = []
    i = 0
    for linha in tabMeteo:
        res.append((tabMeteo[i][0], (tabMeteo[i][2] - tabMeteo[i][1])))
        i = i+1
    
    return res 

def maxChuva(tabMeteo):
    i = 1
    max_data = tabMeteo[0][0]
    max_prec = tabMeteo[0][3]
    while i < len(tabMeteo) -1:
        if tabMeteo[i][3] > max_prec:
            max_prec = tabMeteo[i][3]
            max_data = tabMeteo[i][0]
        i = i +1

    return (max_data, max_prec)


def diasChuvosos(tabMeteo, p):
    res = []
    for x in tabMeteo:
        if x[3] > (p):
            res.append((x[0], x[3]))
    return res


def maxPeriodoCalor(tabMeteo, p):
    contador = 0
    contador2 = 0
    for x in tabMeteo:
        if x[3] < p:
            contador = contador + 1
        else:
            if contador > contador2:
                contador2 = contador
                contador = 0
    return contador2

def guardaTabMeteo(t, fnome):
    f = open(fnome, "w")
    for data, tmin, tmax, precip in t:
        linha = f"{data[0]}::{data[1]}::{data[2]}::{tmin}::{tmax}::{precip}\n"
        f.write(linha)
    f.close()
    return len(t)

def grafTabMeteo(tabMeteo, tipo):
    data = []
    temperaturaMax = []
    temperaturaMin = []
    pluviosidade = []
    for dias in tabMeteo:
        data.append(str(dias[0][0]) + '-' + str(dias[0][1]) + '-' + str(dias[0][2]))
        temperaturaMin.append(dias[1])
        temperaturaMax.append(dias[2])
        pluviosidade.append(dias[3])
    if tipo == 'A':
        matplotlib.pyplot.plot(temperaturaMin, data)
        matplotlib.pyplot.show()
    elif tipo == 'B':
        matplotlib.pyplot.plot(temperaturaMax, data)
        matplotlib.pyplot.show()
    elif tipo == 'C':
        matplotlib.pyplot.plot(pluviosidade, data)
        matplotlib.pyplot.show()
    elif tipo =='D':
        matplotlib.pyplot.plot(temperaturaMin, data)
        matplotlib.pyplot.plot(temperaturaMax, data)
        matplotlib.pyplot.plot(pluviosidade, data)
        matplotlib.pyplot.show()
    
