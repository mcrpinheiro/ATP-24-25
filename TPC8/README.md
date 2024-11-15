# TPC 8: Teste de Aferição
### Autor: Maria Pinheiro 

O TPC 8 consiste numa prova de aferição dos conteúdos lecionados na UC de algoritmos e técnicas de programação. Este TPC foi dividido em 3 partes, que estão resolvidas em 3 ficheiros distintos:
* parte1.py - [Parte 1 do TPC](#tpc-1);
* parte2.py - [Parte 2 do TPC](#tpc-2);
* parte3.py - [Parte 3 do TPC](#tpc-3---rede-social);

## TPC 1
A resolução deste sub tpc encontra-se no ficheiro *parte1.py*. Cada função equivale a uma alínea do exercício proposto:
* `naoComum (lista1, lista2)` - recebe 2 listas e devolve uma nova lista com os elementos que não são comuns às duas listas;
* `palsLongas (texto)` - recebe uma string e devolve uma lista com as palavras da mesma compostas por mais de 3 letras;
* `indiceValor (lista)` - recebe uma lista de string e devolve uma lista de tuplos que corresponde ao indíce de uma palavra na lista e a respetiva palavra.

## TPC 2
A resolução deste sub tpc encontra-se no ficheiro *parte2.py*. Cada função equivale a uma alínea do exercício proposto:
* `contaString (s, subs)` - recebe uma string e uma substring não vazia e devolve o número de vezes em que a substring aparece na string;
* `multiplicaMenor (lista)` - recebe uma lista de inteiros e devolve o resultado da multiplicaçõo dos 3 menores elementos da lista;
* `addDigits(number)` - recebe um número inteiro e devolve o resultado de adicionar repetidamente os seus digitos até obter um só;
* `myIndexOf(s1, s2)` - recebe duas strings e devolve a primeira ocorrência de s2 em s1, ou devolve `-1` no caso de s2 não existir em s1.

## TPC 3 - Rede Social
A resolução deste sub tpc encontra-se no ficheiro *parte3.py*. Para a resolução destes exercícios, consideramos que a informaçao da rede social está armazenada numa lista de dicionários, sendo cada dicionário, um post, com as chaves: `id`, `conteudo`, `autor`, `dataCriacao` e `comentarios`. Por sua vez, `comentarios` é uma lista de dicionários com chaves `comentario` e `autor`.
Cada função equivale a uma alínea do exercício proposto:
* `quantosPost(redeSocial)` - recebe uma rede social, e devolve a quantidade de posts existentes na mesma;
* `postsAutor(redeSocial, autor)` - recebe uma rede social e um autor (string) e devolve a quantidade de posts feito por tal autor;
* `autores(redeSocial)` - recebe uma rede social e devolve uma lista de todos os autores dos posts existentes na rede social, ordenada alfabeticamente;
* `insPost (redeSocial, conteudo, autor, dataCriacao, comentarios)` - recebe uma rede social, 3 strings (conteudo, autor, dataCriacao) e uma lista de dicionarios (comentarios) e devolve a rede social com um novo post com estes parâmetros e com id superior ao último id existente;
* `remPost (redeSocial, id)` - recebe uma rede social e um id (string) e devolve a rede social sem o post com esse mesmo id;
* `postsPorAutor (redeSocial)` - recebe uma rede social e devolve uma distribuição com todos os autores e os seus respetivos posts nessa rede social;
* `comentadoPor (redeSocial, autor)` - recebe uma rede social e um autor e devolve uma lista de todos os posts comentados por esse autor.

