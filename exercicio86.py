#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
import math

jogador = {}
partida = []

jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input("Quantas partidas ele jogou: "))

for c in range(0, tot):
    partida.append(int(input(f'na partida {c} fez quantos gols? ')))

jogador['gols'] = partida[:]
jogador['total'] = sum(partida)

print(jogador)
print(f'=-'*30)
for k, v in jogador.items():
    print(f'no campo {k} tem o valor {v}')
print(f'=-'*30)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} jogos')
for i, v in enumerate(partida):
    print(f'  => na partida {i}, fez {v} gols ')

print(f'Foi um total de {jogador["total"]} gols')