#Faça um programa que leia o comprimeto do cateto oposto e do cateto adjacente de um triângulo retangulo. Calcule e mostre o comprimento da hipotenusa.

import math

n1 = int(input('Digite o valor do cateto oposto: '))
n2 = int(input('Digite o valor do cateto adjacente: '))

hipocalc = math.pow(n1,2) + math.pow(n2,2)
hiporaiz = math.sqrt(hipocalc)

print ('O valor da Hipotenusa nesse calculo é: {:.2f}'.format(hiporaiz))

