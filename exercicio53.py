#Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

print("Painel de Operações!")

num1 = int(input("digite um número: "))
num2 = int(input("digite outro número: "))

while True:
    print("=-=" * 20)
    print(''' 
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    escolha = int(input("Selecione a operação desejada: "))
    if escolha == 1:
        print("o total é: {}".format(num1 + num2))
    elif escolha == 2:
        print("O total é: {}".format(num1 * num2))
    elif escolha == 3:
        if num1 > num2:
            print("O maior é: {}".format(num1))
        elif num2 > num1:
            print("O maior é: {}".format(num2))
        elif num1 == num2:
            print("Os números {} e {} são Identicos!".format(num1,num2))
    elif escolha == 4:
        num1 = int(input("digite um número: "))
        num2 = int(input("digite outro número: "))
    elif escolha == 5:
        print("Saindo do programa...")
        break
    else:
        print("Digite uma opção válida!")



