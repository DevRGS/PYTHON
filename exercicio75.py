# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
listaPar = []
listaImpar = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)
    c = str(input('Quer continuar [S/N]: '))
    if c in 'Nn':
        break
print('-='*30)
print(f'A lista total é: {sorted(lista)}')
print(f'A lista dos pares é: {sorted(listaPar)}')
print(f'A lista dos ímpares é: {sorted(listaImpar)}')