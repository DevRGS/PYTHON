#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesomaior = 0
pesomenor = float(('inf'))
for c in range (0, 3, 1):
    peso = int(input("Digite seu peso: "))
    if peso > pesomaior:
        pesomaior = peso
    elif peso < pesomenor:
        pesomenor = peso
print("O maior peso é: {} e o menor é: {}".format(pesomaior, pesomenor))
