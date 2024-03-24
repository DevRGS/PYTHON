#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um numero pelo telado (entre 0 e 20) e mostrá-lo por extenso.

numExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input("Digite um valor: "))
    if 0 <= n <= 20:
        break
    print('Tente novamente...', end ='')
print(f"Você digitou o número: {numExtenso[n]}")