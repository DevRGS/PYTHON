#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

n1 = float(input('Digite um ângulo: '))

n2_radiano = math.radians(n1)

cos = math.cos(n2_radiano)
tan = math.tan(n2_radiano)
sen = math.sin(n2_radiano)

print('O Cosseno é: {:.4f}/ o Seno é: {:.4f}/ e a Tangente é: {:.4f}'.format(cos, sen, tan))