#Melhore o DESAFIO 55, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print("-=-" *10)
print("Progressão Aritmética")

progressao = int (input("Digite a PA: "))
razao = int (input("Digite a razão: "))
termo = progressao
cont = 1
total = 0
novos = 10
while novos != 0:
    total += novos
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print("PAUSA")
    novos = int(input("Quer mostrar quantos termos a mais: "))
print("Finalizado com o total de: {} Termos mostrados".format(total))