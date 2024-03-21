#Crie um programa que elia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input("Digite o nome completo: ")

if nome.lower().find("silva") != -1:
    print("O nome contém 'SILVA'.")
else:
    print("O nome não contém 'SILVA'.")
