#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

numerosSorteados = []

def sortearValores(valores):
    global numerosSorteados
    numerosSorteados = [randint(0, 10) for _ in range(int(valores))]
    print(f'Temos os números: {numerosSorteados}')

sortearValores(5)

def somarPares():
    pares = cont = 0
    for n in numerosSorteados:
        if n % 2 == 0:
            pares += n
            cont += 1
    print(f'temos ao total {cont} números Pares')
    print(f'Temos ao total {pares} somando os Pares')
    
somarPares()