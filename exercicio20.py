#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import shuffle

nomes = ['rafael', 'gabriel', 'leandro', 'gabriella', 'gabrielle']

shuffle(nomes)

print (nomes[0])