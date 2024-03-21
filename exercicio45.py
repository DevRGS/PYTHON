#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

p = int(input("Digite o termo: "))
r = int(input("Digite a razão: "))
ramo = int (input("Até onde vai: "))

for c in range (p, ramo+1, r):
    print(c, "> ", end =" ")
print("ACABOU")