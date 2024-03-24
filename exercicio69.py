#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.


num = (int(input("Digite um valor: ")),
       int(input("Digite outro valor: ")),
       int(input("Digite mais um valor: ")),
       int(input("Digite um ultimo valor: "))
       )

print(f'Os números mostrados foram: {num}')
print(f'o número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o número 3 foi encontrado na {num.index(3)}° posição')
else:
    print('O número 3 não foi encontrado')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')
