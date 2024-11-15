# TPC 3: Jogo dos 21 Fósforos
## Autor: Maria Pinheiro

O TPC 3 consiste na realização de uma aplicação para jogar o jogo dos 21 fósforos. Este foi dividido em 2 ficheiros:
* *menu.py* - onde se encontra a aplicação principal;
* *tpc3.py*  - onde estão as funções para correr o jogo.

### Informações sobre o jogo:
* No início do jogo há 21 fósforos;
* Cada jogador pode tirar entre 1 a 4 fósforos de cada vez;
* As rondas são alternadas;
* Perde o jogador que tirar o último fósforo.

### A aplicação do jogo
Nesta aplicação, o utilizador pode escolher entre jogar primeiro, ou o computador jogar primeiro. Considerando isto, o menu questiona ao utilizador quem vai jogar primeiro e consoante a escolha, corre a função destinada.
* (1) Utilizador - o utilizador joga primeiro. Neste modo, o computador deve sempre ganhar.
* (2) Computador - o computador joga primeiro. Neste modo, o computador deve ganhar se o utilizador fizer um erro de cálculo.

### Funções do jogo
Considerando que existem 2 tipos de modos de jogo, criei 2 funções principais, uma para cada modo, no ficheiro *tpc3.py*.
* `userPlays()` - função que é corrida quando o jogador escolhe jogar primeiro;
* `pcPlays()` - função que é corrida quando o jogador escolhe jogar em segundo lugar.

