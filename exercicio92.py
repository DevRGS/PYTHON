 #Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
 
from random import randint
from time import sleep

def linhas():
    print('-=' * 20)
    

def maioresNumeros(cont, passo):    
    while True:
        if cont >= 0 :
            def randomm():
                return (randint(0,200))

            numeros = [randomm() for _ in range (int(cont))]

            for i, n in enumerate(numeros):
                print(f' {n} ', end='')
                sleep(0.2)

            print()
            print(f'Temos no total {len(numeros)} valores')
            print(f'O maior valor mostrado é --{max(numeros) if len(numeros) != 0 else 0}--')
            linhas()
            
            cont -= passo
        
        else:
            print("Finalizando!")
            linhas()
            break

maioresNumeros(10, 2)



 
