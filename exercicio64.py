# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.

totalCompra = precoMaisBarato = maisdeMil = cont = 0
nomeMaisBarato = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = int(input('Digite o valor do produto: '))
    totalCompra += preco
    cont += 1
    if preco >= 1000:
        maisdeMil += 1
    if cont == 1 or preco < precoMaisBarato:
        precoMaisBarato = preco
        nomeMaisBarato = nome
    escolha = str(input("Quer continuar? [S/N]: ")).upper()
    if escolha == 'N':
        break
print(f'O total da compra daria: {totalCompra}')
print(f'Tiveram {maisdeMil} produtos que valem mais de 1000')
print(f'o nome do produto mais barato é {nomeMaisBarato} e tem valor de R$ {precoMaisBarato}')