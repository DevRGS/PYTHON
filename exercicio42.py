#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print("Números multiplos de 3")
saldo = 0
cont = 0
for c in range(1,501,2 ):
    if c % 3 == 0:
        saldo = saldo + c
        cont = cont + 1
print("A soma de todos {} valores, é : {}".format(cont, saldo))
print("fim")