#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0,], [0, 0, 0,]]
par = terceira = maior = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor na posição {l}, {c}: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            terceira += matriz[l][c]

maior = max(matriz[1])
print('*-'*30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('*-'*30)
print(f'a Soma dos pares é {par}')
print(f'a Soma dos valores da terceira coluna é {terceira}')    
print(f'o Maior valor da segunda linha é {maior}')