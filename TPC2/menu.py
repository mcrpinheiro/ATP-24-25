from tpc2 import userGuesses, pcGuesses

def menu():

    jogo = input('Quer adivinhar (1), escolher um número(2) ou sair do jogo(0)?')
    while jogo != '0':
        if jogo == '1':
            userGuesses()
            jogo = input('Deseja adivinhar(1), escolher um número(2) ou sair do jogo(0)?')
        elif jogo == '2':
            pcGuesses()
            jogo = input('Deseja adivinhar(1), escolher um número(2) ou sair do jogo(0)?')
        else:
            jogo = input('Opção não suportada, tente outra vez. Quer adivinhar(1), escolher um número(2) ou sair do jogo (0)?')
    print('Obrigado, volte sempre!')
menu()
