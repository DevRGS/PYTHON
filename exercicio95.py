#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

#def fatorial (num, show = False):
#    if show == True:
#        for c in range (num, 0, 1):
#            print(f'{c} - {num}', end=' ')
#            
#            total = num * c
#    else:
#        for c in range (num, 0, 1)

def fatorial(n, show=False):
    resultado = 1
    contagem = []

    for i in range(n, 0, -1):
        resultado *= i
        contagem.append(str(i))

    if show:
        # Exibe o processo de cálculo do fatorial
        print(f"O fatorial de {n} é:")
        print(" x ".join(contagem) + f" = {resultado}")
    else:
        # Exibe apenas o resultado
        print(f"O fatorial de {n} é {resultado}")

# Solicita ao usuário que insira um número
numero = int(input("Digite um número: "))
mostrar_calculo = input("Deseja mostrar o cálculo? (s/n): ").lower() == 's'

fatorial(numero, show=mostrar_calculo)


            