pessoas = list()
dados = list()
totmaior = totmenor = 0

for c in range (0,3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    pessoas.append(dados[:])
    dados.clear()

for p in pessoas: 
    if p[1] > 18:
        totmaior += 1
        print(f'a {p[0]} é maior de idade')
    else:
        totmenor += 1
        print(f'a {p[0]} é menor de idade')
    
print(f'No total, tivemos {totmaior} maiores de idade e {totmenor} menores de idade')