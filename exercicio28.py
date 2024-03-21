#Faça um programa que lea um frase pelo teclado e mostre:

#Quantas vezes aparece a letra "A".

#Em que posição ela aprece a primeira vez.

#Em que posição ela aprece na última vez.

frase = input("Digite uma frase: ")

# Contando o número de vezes que a letra 'A' aparece na frase
quantidade_a = frase.lower().count('a')

# Encontrando a posição da primeira ocorrência da letra 'A'
primeira_posicao = frase.lower().find('a')

# Encontrando a posição da última ocorrência da letra 'A'
ultima_posicao = frase.lower().rfind('a')

print("Quantidade de vezes que 'A' aparece na frase:", quantidade_a)
print("Primeira posição de 'A':", primeira_posicao)
print("Última posição de 'A':", ultima_posicao)
