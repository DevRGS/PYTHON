# Crie um programa que leia duas notas de um aluno e calcule sua média, # mostrando uma mensagem no final, de acordo com a média atingida:

# – Média abaixo de 5.0: REPROVADO

# – Média entre 5.0 e 6.9: RECUPERAÇÃO

# – Média 7.0 ou superior: APROVADO

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

resul = (n1 + n2) / 2

print("Dada a sua média {} pontos:".format(resul))
if resul < 5:
    print("Você esta de reprovado!")
elif resul >= 7:
    print("Você esta aprovado!")
else:
    print("Você esta de Recuperação!")