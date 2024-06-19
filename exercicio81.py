#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from time import sleep
from random import randint

temp = list()
jogos = list()
print('-'*30)
print(' '*3, 'Mega Sena Hacked', ' '*3 )
print('-'*30)
apostas = int(input('Quantas apostas você quer hoje: '))
tot = 1
while tot <= apostas:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in temp:
            temp.append(num)
            cont += 1
        if cont >= 6:
            break
        
    temp.sort()
    jogos.append(temp[:])
    temp.clear()    
    tot += 1
        
print(' '*3, f'<- Sorteando {apostas} jogos! ->', ' '*3)

for i, l in enumerate(jogos):
    print(f'{i+1}° jogo: {l}')
print('-='*5, ' <- Boa Sorte -> ','-='*5)