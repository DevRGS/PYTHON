n1 = int(input ('Digite um numero: '))
n2 = int(input ('Digite outro numero: '))
a = n1 + n2
s = n1 - n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
r = n1 % n2
raiz = n1 **(1/2)

print ('A Soma é {}, a Subtração é {}, a Divisão é {}'.format(a, s, d))
print ('A Potência é {}, a Divisão Interia é {:.3f}'.format(p ,di))
print ('O Resto da Divisão é {}, e a Raiz Quadrada é {}'.format(r, raiz))