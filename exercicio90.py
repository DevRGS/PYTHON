#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#Ex:
#
#(‘Olá, Mundo!’) Saída:
#
#~~~~~~~~~
#Olá, Mundo!
#~~~~~~~~~

def centralizar_palavra(palavra_top):
    tamanho_palavra = len(palavra_top) + 10
    tils = '~' * tamanho_palavra
    palavra_centralizada = palavra_top.center(tamanho_palavra)
    
    print(tils)
    print(palavra_centralizada)
    print(tils)
    
centralizar_palavra(input("Digita aqui: "))