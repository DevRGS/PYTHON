#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = input("Digite o nome da cidade: ")

# Convertendo a cidade para letras minúsculas para facilitar a comparação
cidade = cidade.strip().lower()

if cidade[:5] == "santo":
    print("O nome da cidade começa com 'SANTO'.")
else:
    print("O nome da cidade não começa com 'SANTO'.")
