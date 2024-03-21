#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Exemplo: Digite um numero: 6.127.
#O numero 6.127 tem a porção inteira 6.

import math

n1 = float(input('Digite um numero qualquer: '))

n2 = math.ceil(n1)

print ('O numero {} tem a porção inteira {}'.format(n1, n2))