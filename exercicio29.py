#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro nome e o último nome separadamente.

#EX: Ana Maria de Souza.

#Primeiro: Ana
#Ultimo: Souza

nome_completo = input("Digite seu nome completo: ")

# Separando as partes do nome usando o espaço como delimitador
partes_nome = nome_completo.split()

# Acessando o primeiro e o último nome da lista resultante
primeiro_nome = partes_nome[0]
ultimo_nome = partes_nome[-1]

print("Primeiro nome:", primeiro_nome)
print("Último nome:", ultimo_nome)
