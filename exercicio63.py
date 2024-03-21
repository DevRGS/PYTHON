#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

totalPessoas = totalHomens = totalMulheres = 0
while True:
    idade = int(input("Digite a Idade: "))
    sexo = str(input("Digite o Sexo [M/F]: ")).strip().upper()[0]
    if idade >= 18:
        totalPessoas += 1
    if sexo == 'M':
        totalHomens += 1
    if idade < 20 and sexo == 'F':
        totalMulheres += 1

    escolha = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if escolha == 'N':
        break
print(f'Tivemos {totalMulheres} mulheres com menos de 20 anos')
print(f'Tivemos {totalHomens} homens cadastrados')
print(f'Tivemos {totalPessoas} pessoas com mais de 18 anos')

