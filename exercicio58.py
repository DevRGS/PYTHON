#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = int(input("Digite um número inteiro: "))
cont = 0
tot = 0

while n != 999:
    tot += n
    cont += 1
    n = int(input("Digite um outro número inteiro [digite 999 para parar]: "))
print("a soma total dos números é: {}, e foram digitados {} números".format(tot, cont))