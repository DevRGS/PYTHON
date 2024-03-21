#Desenvolva um programa que leia 
# o nome, 
# idade 
# sexo de 4 pessoas. 
# No final do programa, mostre:  
# a média de idade do grupo, 
# qual é o nome do homem mais velho e 
# quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridade = 0
nomehomemvelho = ''
mulheres = 0

for pess in range (1, 5, 1):
    print("-"*5,"°{} PESSOA".format(pess),("-"*5))
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    genero = str(input("Digite seu gênero M/F: ")).upper()
    somaidade += idade
    
    if pess == 1 and genero in ('Mm'):
        nomehomemvelho = nome
        maioridade = idade
    if genero in ('Mm') and idade > maioridade:
        nomehomemvelho = nome
        maioridade = idade    
    if genero in 'Ff' and idade < 20:
        mulheres += 1
        
mediaidade = somaidade / pess
print("a média de idade do grupo é: {:.2f}".format(mediaidade))
print("O nome do homem mais velho é: {}, tendo {} anos".format(nomehomemvelho, maioridade))
print("Neste grupo, temos {} mulheres com menos de 20 anos".format(mulheres))