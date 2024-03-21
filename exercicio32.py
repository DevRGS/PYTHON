#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– SE O primeiro valor é maior
#– SE O segundo valor é maior
#– Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O {} é Maior'.format(n1))
elif n2 > n1:
    print('O {} é Maior'.format(n2))
else:
    print('Os números são Iguais!')
    