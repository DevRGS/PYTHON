#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista, caso se repitam, mostre em que posição foi repitido.

valores = []
maior = menor = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite o {c}° valor: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('-='*20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior}, e apareceu nas posições ',end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O menor valor digitado foi {menor}, e apareceu nas posições ',end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end='')
print()

