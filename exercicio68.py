#Crie um programa que vai gerar cinco números aletórios e colocar em uma tupla.

#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

pc = (
    randint(0,10),
    randint(0,10),
    randint(0,10),
    randint(0,10),
    randint(0,10)
)

print(f'Os números gerados foram: {pc}')

maior = max(pc)
menor = min(pc)

print(f'O Maior valor é {maior}')
print(f'O Menor valor é {menor}')
