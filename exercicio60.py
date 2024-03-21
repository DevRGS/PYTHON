#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quadno o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (Descondiserando o flag)

n = cont = s = 0

while True:
    n = int(input("Digite um valor: "))
    if n == 999:
        break
    cont += 1
    s += n
print(f'o total é {s} e você digitou {cont} valores')