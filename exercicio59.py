# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = cont = maior = menor = media = 0

while resp in 'Ss':
    num = int(input("Digite um número inteiro: "))
    soma += num
    cont += 1
    if cont == 1:
        menor = maior = num
    else:
        if  num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N] "))

media = soma / cont
print("o Total é {}, e foram digitados {} números".format(soma, cont))
print("O maior número é {},o menor é {}, e a média é {}".format(maior,menor,media))
