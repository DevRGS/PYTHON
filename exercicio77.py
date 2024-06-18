#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.


pessoas = list()
temp = list()
mai = men = 0

while True:
    temp.append(str(input("Digite o Nome: ")))
    temp.append(float(input("Digite o seu Peso: ")))
    if len(pessoas) == 0:
        mai = temp[1]
        men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1] 
        if temp[1] < men:
            men = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-'*30)
print(f"No total tivemos {len(pessoas)} cadastradas")
print(f'O maior peso foi de {mai}Kg, Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg, Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')