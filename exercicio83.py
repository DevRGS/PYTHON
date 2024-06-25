#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# Abaixo de 5 = Reprovado
# Abaixo de 7 = Recuperação
# Acima de 7 = Aprovado

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))

if aluno['media'] <= 5:
    aluno['situação'] = 'Reprovado'
    
elif aluno['media'] > 5 and aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'

else:
    aluno['situação'] = 'Aprovado'
print('-_'*30)

for k, v in aluno.items():
    print(f'    - {k} é igual a {v}')
    
