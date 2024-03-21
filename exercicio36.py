#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
#– EQUILÁTERO: todos os lados iguais
#
#– ISÓSCELES: dois lados iguais, um diferente
#
#– ESCALENO: todos os lados diferentes


t1 = float(input("Digite o tamanho do primeiro lado do triângulo: "))
t2 = float(input("Digite o tamanho segundo lado do triângulo: "))
t3 = float(input("Digite o tamanho terceiro lado do triângulo: "))

print("Analisando seu Triângulo...")

if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print("Os segmentos apresentados podem formar um triângulo: ",end='')
    if t1 == t2 == t3:
        print("EQUILÁTERO")
    elif t1 != t2 != t3 != t1:
        print("ESCALENO")
    else: 
        print("ISÓSCELES")
else:
    print("pra começa, isso nem é um triângulo, mula")
    