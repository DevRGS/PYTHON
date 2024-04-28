# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:                                                                                                                                                A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    c = str(input('Quer continuar? [S/N]'))
    if c in 'nN':
        break
print('=-='*20)
print(f'Tivemos {len(lista)} valores digitados')
print('=-='*20)
print(f'Em ordem Descrecente: {sorted(lista,reverse=True)}')
print('=-='*20)
if 5 in lista:
    print('o Valor 5 foi digitado, e esta na lista')
else:
    print('o Valor 5 não esta na lista')

