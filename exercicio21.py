#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a sequencia.

import random

nomes = ['rafael', 'gabriel', 'gabrielle', 'gabriella', 'danielle']

shuffle = (nomes)

for n, (c1) in enumerate(zip(nomes), start=1):

    print (f'   Sequencia dos Trabalhos {n}')
    print (f' {c1}')