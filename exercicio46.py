#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

i = int(input("Onde começa: "))
fim = int(input("Onde termina: "))
tot = 0
cores = {
    'limpa': '\033[m',
    'azul': '\033[0;34m',
    'red': '\033[0;31m',
    'destaque': '\033[7;30m',
    'amarelo': '\033[0;33m',
    'verde': '\033[0;32m'
}

for c in range(i, fim +1, 1):
    if c >= 1:
        primo = True
        for i in range (2, c):
            if (c % i) == 0:
                print(c, "{}Não{} é um {}número primo{}".format(
                    cores['red'],
                    cores['limpa'],
                    cores['amarelo'],
                    cores['limpa']
                ))
                primo = False
                break
        if primo:
            tot += 1
            print(c, "{}È{} um {}número prima{}, é {}dentro{}".format(
                cores['verde'],
                cores['limpa'],
                cores['azul'],
                cores['limpa'],
                cores['verde'],
                cores['limpa']
            ))
print("até o número {}, existem {}`números primos".format(fim, tot))
        
