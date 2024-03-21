# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
impar = 0
for c in range (0, 6+1 ,1):
    n = int(input("Digite um número inteiro: "))
    if n % 2 == 0:
        soma += n
        cont += 1
    elif n % 2 >= 1:
            impar += 1

print("A soma de todos os {} valores PARES é {}, e foram descosiderados {} números impáres".format(cont, soma, impar))