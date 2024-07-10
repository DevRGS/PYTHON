#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

galera = []
pessoas = {}

media = tot = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F] ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print("ERRO! válido apenas resposta M ou F")

    pessoas['idade'] = int(input('Digite sua idade: '))
    tot += pessoas['idade']
    galera.append(pessoas.copy())
    
    resp = str(input("Quer continuar? [S/N] "))
    if resp in 'Nn':
        break

media = tot / len(galera)
print('=-'*30)
print(f'A) foram cadastradas {len(galera):5.2f} pessoas')
print(f'B) a Média de idade do grupo é {media}')

print(f'C) as Mulheres da lista são: ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()

print(f'D) as pessoas com idade acima da média são: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' | ')
print()
print(f'        <<ENCERRADO>>       ')


