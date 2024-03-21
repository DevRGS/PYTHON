#Faça que leia um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex:

#Digite um número: 1834

#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1

num = int(input("Digite um número entre 0 e 9999: "))

uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print("Unidade: {}".format(uni))
print("Dezena: {}".format(dez))
print("Centena: {}".format(cen))
print("Milhar: {}".format(mil))