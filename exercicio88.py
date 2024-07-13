#Aprimore o desafio 86 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

import math

time = []
jogador = {}
partida = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).upper()
    tot = int(input("Quantas partidas ele jogou: "))
    partida.clear()
    
    for c in range(0, tot):
        partida.append(int(input(f'na partida {c} fez quantos gols? ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    
    while True:
        resp = str(input("Quer continuar? [S/N]")).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break 
    
print('=-' * 30)
print('COD ', end='')
for i in jogador.keys():
    print(f'{i:<15}'.upper(), end='')
print()
print('=-'* 30)
for k, v in enumerate(time):
    print(f'{k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end ='')
    print()
print('=-'*30)      

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! não existe jogador com o código {busca}!')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('=-' * 30)
print(f'   << VOLTE SEMPRE >>   ')