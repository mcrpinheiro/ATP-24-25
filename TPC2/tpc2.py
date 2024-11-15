import random

def userGuesses ():
    guess = int(input('O número que escolhi está entre 0 e 100. Consegue descobrir qual é?'))
    number = random.randint(0,100)  
    ntentativas = 1 

    while guess != number:
        if guess>number:
            guess = int(input('Errado. O número que escolhi é menor! Tente outra vez:'))
            ntentativas = ntentativas + 1
        else:
            guess = int(input('Errado. O número que escolhi é superior. Tente outra vez:'))
            ntentativas = ntentativas + 1
    print(f'Parabéns, acertou em {ntentativas} tentivas!')

def pcGuesses ():
    found = False
    guess = random.randint(0,100)
    ntentativas = 1
    min = 0
    max = 100
    while not found:
        result = input(f'O meu número é {guess}. Está correto? S/N')
        if result == 'S' or result =='s':
            found = True
        else:
            ran = input(f'O seu número é superior(+) ou inferior(-) a {guess}?')
            if ran == '+':
                min = guess + 1
                guess = random.randint(min, max)
                ntentativas = ntentativas + 1
            elif ran =='-':
                max = guess - 1
                guess = random.randint(min, max)
                ntentativas = ntentativas + 1
            else:
                ran = input(f'Opção não suportada, tente outra vez. O seu número é superior (+) ou inferior (-) a {guess}?')

    print(f'Ótimo, acertei em {ntentativas} tentivas!')

