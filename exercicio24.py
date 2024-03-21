#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#o Nome com todas as letras minúsculas
#Quantas letras ao todo sem considerar os espaços
#quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: "))
nomeE = nome.strip()
nomeP = nome.split()
print('Seu nome com letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome com letras minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras ao todo sem considerar os espaços: {}'.format(len(nome) - nome.count(' ')))
print('Quantidade de letras do primeiro nome: {}'.format(len(nomeP[0])))
