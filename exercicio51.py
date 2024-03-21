#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Informe seu Sexo M/F: ")).strip().upper()[0]

while sexo not in ('MmFf'):
    sexo=str(input("Dados invalidos! Digite seu sexo novamente: ").strip().upper())[0]
print("Excelente, Sexo {}, Detectado!".format(sexo))


