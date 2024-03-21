n1 = int(input('Digite quantos metros de Altura a parede tem: '))
n2 = int(input('Digite quantos metros de Largura a parede tem: '))

a = n1*n2
t = a/2

print('Perfeito, a Àrea total é {} Metros, você irá precisar de {:.3f} Litros de Tinta para Pinta-la'.format(a, t))