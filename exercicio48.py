#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

print("Analizando maioridade")

hoje = date.today().year
maiores = 0
menores = 0

for pessoas in range (1, 8, 1):
    nasc = int(input("em que ano {}° nasceu: ".format(pessoas)))
    idade = hoje - nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print("Tivemos {} de maior, e {} pessoas de menor".format(maiores, menores))

