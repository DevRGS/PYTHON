# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
# e também diga quantos valores existem em cada lista.

nums = [[], []]
valor = 0

for c in range (1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        nums[0].append(valor)
    else:
        nums[1].append(valor)
print("*-"*30)

nums[0].sort()
nums[1].sort()

print(f'Tivemos {len(nums[0])} valores pares, sendo eles: {nums[0]}')
print(f'Tivemos {len(nums[1])} valores impáres, sendo eles: {nums[1]}')


