#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#
#– IMC abaixo de 18,5: Abaixo do Peso
#
#– Entre 18,5 e 25: Peso Ideal
#
#– 25 até 30: Sobrepeso
#
#– 30 até 40: Obesidade
#
#– Acima de 40: Obesidade Mórbida

print("-=-"*20)
print("Calculo de IMC")
print("-=-"*20)

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura**2)

print("Seu IMC é {:.2f}, e você esta na categoria: ".format(imc), end ='')

if imc > 40:
    print("OBESIDADE MORBIDA")
elif imc > 29:
    print("OBESIDADE")
elif imc > 24:
    print("SOBREPESO")
elif imc > 18.4:
    print("PESO IDEAL")
else:
    print("ABAIXO DO PESO")
