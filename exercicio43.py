#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print("Tabuada V2.0")

num = int(input("Digite o número que você quer a tabuada: "))
tab = int(input("Até qual tabuada você quer ver: "))

for c in range(0, tab+1, 1):
    print(c, "x", tab, "=", tab*c)
print("fim")