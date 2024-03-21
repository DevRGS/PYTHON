# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print('=-=' * 10)
print("JOGO DO PAR OU ÍMPAR")
print('=-=' * 10)

v = 0
while True:
    jogador = int(input("Escolha um número: "))
    pc = randint(0, 10)
    aposta = ' '
    total = jogador + pc
    resultado = ''
    while aposta not in 'PI':
        aposta = str(input("PAR ou ÍMPAR? [P/I]: ")).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {pc}, total de: {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if aposta == 'P':
        if total % 2 == 0:
            print("Você ganhou!")
            v += 1
        else:
            print("Você PERDEU!")
            break
    elif aposta == 'I':
        if total % 2 == 1:
            print("Você ganhou!")
            v += 1
        else:
            print("Você PERDEU!")
            break
    print("Vamos jogar novamente...")
print(f'GAME OVER! você ganhou {v} vez!' if v < 1 else f'GAME OVER! você ganhu {v} vezes seguidas!')
