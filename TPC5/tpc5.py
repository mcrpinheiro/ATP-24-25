import random
from random import sample

def criarCinema():
    cinema = []
    i = random.randint(1, 10)
    while i > 0:
        nlugares = random.randint(10, 50)
        nrvendidos = random.randint(1,nlugares)
        vendidos = sample(range(1,nlugares),nrvendidos)
        filme = random.choice([
        "The Godfather",
        "Forrest Gump",
        "Inception",
        "Fight Club",
        "The Lord of the Rings: The Fellowship of the Ring",
        "The Matrix",
        "Joker",
        "Saving Private Ryan",
        "Interstellar",
        "Parasite",
        "Amélie",
        "Pulp Fiction",
        "The Shining",
        "Toy Story",
        "Life is Beautiful"
])
        cinema.append([nlugares, vendidos , filme])
        i = i -1
    return cinema

def verCinema(cinema):
    i = 1
    s = ''
    for c in cinema:
        s = s + (f'Sala {i} - {c[0]} Lugares Totais - {len(c[1])} Lugares Ocupados {c[1]} - Filme: {c[2]} \n')
        i = i+1
    return s

def listar(cinema):
    s = []
    for c in cinema:
        s.append(c[2])
    return s

def disponivel (cinema, filme, lugar):
    sala = []
    res = False
    for s in cinema:
        if s[2] == filme:
            sala = s  
    if sala == []:
        res = False     
    if int(lugar) not in sala[1]:
        res = True
    return res

def vendebilhete (cinema, filme, lugar):
    for s in cinema:
        if s[2] == filme:
            if int(lugar)>s[0]:
                print('Este lugar não existe!')
            else:
                s[1].append(int(lugar))
    return cinema


def listardisponibilidades(cinema):
    i = 1
    s = ''
    for c in cinema:
        s = s + (f'Sala {i}: Filme {c[2]} com {c[0] - len(c[1])} lugares disponíveis.\n')
        i = i + 1
    return s

def inserirSala(cinema,sala):
    if sala in cinema:
        print('Esta sala já existe neste cinema.')
    else:
        cinema.append(sala)
    return cinema
    



