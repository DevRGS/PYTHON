#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
#
#
#FORMA 1
#def fatorial(num, show = False):
#   f = 1
#   for c in range (num, 0, -1):
#       f *= c
#       if show:
#           print(f'{c}' ,  end = '')
#           if c > 1:
#               print(' x ', end = '')
#           else:
#               print(' = ', end = '')
#   return f
#        
#nume = int(input("digite um numero para ver seu fatorial: "))
#resul = input("Mostrar resultado? [S/N ]").lower() == 's'
#
#resultado = fatorial(nume, resul)
#
#print(resultado)
#


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


            