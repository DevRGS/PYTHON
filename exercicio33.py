#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

hoje = date.today().year
idade = int(input('Digite seu ano de nascimento: '))
alist = hoje - idade

print("Quem nasceu em {}, tem {} em {} ".format(idade, alist, hoje))

if alist == 18:
    print("Você deve se alistar Imediatamente!")
elif alist > 18:
    saldo = alist - 18
    print("Você já deveria ter se alistado a {} Anos!".format(saldo))
else:
    saldo = 18 - alist
    print("Você ainda não pode se alistar! você deve se alistar daqui: {} Anos!".format(saldo))




