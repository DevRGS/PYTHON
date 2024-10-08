#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            
#    a) de 1 até 10, de 1 em 1                                                                                                                                              
#    b) de 10 até 0, de 2 em 2                                                                                                                                            
#    c) uma contagem personalizada

from time import sleep

def linhas ():
    print('-=' * 20)
    

def contador(i, f, p):
    
    if p == 0:
        p = 1
    
    if p < 0:
        p *= -1
        
    print(f'contando de {i} até {f} de {p} em {p}')
    sleep(2)
    
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end = '', flush=True)
            cont += p
            sleep(0.3)
        print('FIM')
        linhas()
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end = '', flush=True)
            cont -= p
            sleep(0.3)
        print('FIM')
        linhas()
        
contador( 0, 10, 1)
contador(10, 0, 2)

linhas()

print('Agora é sua vez! ')

inicio = int(input('Inicio:  '))
fim = int(input('Fim:        '))
passo = int(input('Passo:    '))

contador(inicio, fim, passo)