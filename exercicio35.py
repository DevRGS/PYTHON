#A Confederação Nacional de Natação precisa de um programa que leia o #ano de nascimento de um atleta e mostre sua categoria, de acordo com a #idade:
#
#– Até 9 anos: MIRIM
#
#– Até 14 anos: INFANTIL
#
#– Até 19 anos: JÚNIOR
#
#– Até 25 anos: SÊNIOR
#
#– Acima de 25 anos: MASTER

from datetime import date

idade = int(input("Digite sua data de nascimento: "))
hoje = date.today().year
classe = hoje - idade

print("Você tem hoje {} anos, logo:".format(classe))
if classe > 25:
    print("Você é da Classe MASTER")
elif classe > 19:
    print("Você é da Classe SÊNIOR")
elif classe > 14:
    print("Você é da Classe JÚNIOR")
elif classe > 9:
    print("Você é da Classe INFANTIL")
else:
    print("Você é da Classe MIRIM")

