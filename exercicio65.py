# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


notaDuzentos = 200
notaCem = 100
notaCinquenta = 50
notaVinte = 20
notaDez = 10
notaUm = 1

contDuzentos = contCem = contCinquenta = contVinte = contDez = contUm = 0
n = int(input("digite um valor: "))

while True:
    if n >= notaDuzentos:
        n -= notaDuzentos
        contDuzentos += 1

    elif n >= notaCem:
        n -= notaCem
        contCem += 1

    elif n >= notaCinquenta:
        n -= notaCinquenta
        contCinquenta += 1

    elif n >= notaVinte:
        n -= notaVinte
        contVinte += 1

    elif n >= notaDez:
        n -= notaDez
        contDez += 1

    elif n >= notaUm:
        n -= notaUm
        contUm += 1

    else:
        break

if contDuzentos >0:
    print(f'Foram utilizadas {contDuzentos} notas de Duzentos Reais')
if contCem > 0:
    print(f'Foram utilizadas {contCem} notas de Cem Reais')
if contCinquenta > 0:
    print(f'Foram utilizadas {contCinquenta} notas de Cinquenta Reais')
if contVinte > 0:
    print(f'Foram utilizadas {contVinte} notas de Vinte Reais')
if contDez > 0:
    print(f'Foram utilizadas {contDez} notas de Dez Reais')
if contUm > 0:
    print(f'Foram utilizadas {contUm} notas de Um Real')
