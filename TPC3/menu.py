from tpc3 import userPlays, pcPlays

def menu():
    opcao = input('''Bem vindo ao jogo dos fósforos! Quem vai jogar primeiro?
    (1) Utilizador
    (2) Computador
    (0) Sair''')
    novaopcao = '''Quem vai jogar primeiro desta vez?
    (1) Utilizador
    (2) Computador
    (0) Sair'''
    while opcao != '0':
        if opcao == '1':
            print(userPlays())
            opcao = input(novaopcao)
        elif opcao == '2':
            print(pcPlays())
            opcao = input(novaopcao)
        else:
            print('Opção não disponível, tente outra vez!')
            opcao = input(novaopcao)
    print('Obrigada por jogar! Volte sempre.')

menu()