# TPC 2: Jogo de Adivinha o Número
### Autor: Maria Pinheiro

O TPC 2 consiste na realização de uma aplicação para jogar o jogo de adivinha o número. Este foi dividido em 2 ficheiros:
* *menu.py* - onde se encontra a aplicação principal;
* *tpc2.py*  - onde estão as funções para correr o jogo.

### Informações sobre o jogo:
* O número escolhido é entre 0 e 100;
* Quem escolher o número indica se o número escolhido é igual, superior, ou inferior;
* Quando o número é acertado, o número de tentativas é imprimido.

### A aplicação do jogo
Nesta aplicação, o utilizador pode escolher entre escolher um número ou adivinhar o número que o computador escolheu.. Considerando isto, o menu questiona ao utilizador se quer escolher um número ou adivinhar:
* 'Quer adivinhar (1)' - o utilizador tenta então, adivinhar o número que o computador escolhe aleatoriamente.
* 'escolher um número (2)' - o utiliador escolhe um número para o computador adivinhar.

### Funções do jogo
Considerando que existem 2 tipos de modos de jogo, criei 2 funções principais, uma para cada modo, no ficheiro *tpc2.py*.
* `userGuesses()` - função que é corrida quando o jogador escolhe adivinhar;
* `pcGuesses()` - função que é corrida quando o jogador escolhe escolher um número.
