import random

def userPlays ():
    vencedor = 'Lamento, o computador venceu.'
    fosforos = 21
    jogadas = 1
    while fosforos > 1 :
        if jogadas%2 !=0:
            uplay = int(input('Escolha a sua jogada.'))
            if uplay not in [1,2,3,4] or uplay>fosforos: 
                print('Jogada errada, tente outra vez')    
            else:    
                print(f'Utilizador jogou: {uplay}')
                jogadas = jogadas + 1
                fosforos = fosforos - uplay
        else:
                pcplay = 5 - uplay
                fosforos = fosforos - pcplay
                jogadas = jogadas + 1
                print(f'Computador jogou: {pcplay}')
        print(f'Fosforos restantes: {fosforos}')
    return vencedor 

def pcPlays ():
    vencedor = 'Parabéns, venceu o jogo!'
    fosforos = 21
    jogadas = 1
    while fosforos != 1:
        if jogadas%2 ==0:
            uplay = int(input('Escolha a sua jogada.'))
            if uplay not in [1,2,3,4] or uplay>=fosforos: 
                print('Jogada errada, tente outra vez!')    
            else:    
                print(f'Utilizador jogou: {uplay}')
                jogadas = jogadas + 1
                fosforos = fosforos - uplay
        else:
            if fosforos <= 5:
                pcplay = fosforos - 1
                fosforos = fosforos - pcplay
                vencedor = 'Lamento, o computador venceu.'
            else:
                pcplay = random.randint(1,4)
                jogadas = jogadas + 1
                fosforos = fosforos - pcplay
                print(f'Computador jogou: {pcplay}')
        print(f'Fosforos restantes {fosforos}')
    return vencedor


    