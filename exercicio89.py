#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'O tamanho do terreno {larg}m² x {comp}m² é de {a:.2f}m²')


print()
print('-'*5 + ' Calculadora de Terreno ' + '-'*5)
print()
l = float(input('Digite a Largura do terreno em m²: '))
c = float(input('Digite o Comprimento do terreno em m²: '))
area(l, c)
print()