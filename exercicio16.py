#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input("Quantos dias você utilizou o carro: "))

kms = float(input("Quantos KM você percorreu com o carro: "))

total = (dias * 60) + (kms * 0.15)

print ("Perfeito! o total a pagar ficou em R${:.2f}".format(total))
