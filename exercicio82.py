#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Continuar? [S/N] '))
    if resp in 'Nn':
        break

print('_'*30)
print(f'{"No.":<6}{"Nome":<10}{"Média":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<6}{a[0]:<10}{a[2]:>8}')

while True:
    notas = int(input('Quer ver as notas de qual aluno? (999 finaliza)'))
    if notas == 999:
        print("Saindo do Programa...")
        break
    
    if notas <= len(ficha) - 1:
        print(f'as Notas de {ficha[notas][0]} são: {ficha[notas][1]}')
        