#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

print("Analizando Palídromo")
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print("Você digitou a frase: {}".format(frase))
for letra in range(len(junto) -1 ,-1, -1):
        inverso += junto[letra]
print("A frase: {}, ao inverso é: {}".format(junto, inverso))
if inverso == junto:
    print("é um PALÍNDROMO")
else:
    print("não é um PALÍNDROMO")
    
#Pode funcionar da mesma forma sem o loop for, colocando:
#inverso = junto[::-1]