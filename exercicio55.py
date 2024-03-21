#leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("-=-" *10)
print("Progressão Aritmética")

progressao = int (input("Digite a PA: "))
razao = int (input("Digite a razão: "))
termo = progressao
cont = 1

while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print("Fim")