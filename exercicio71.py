#Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.

palavras = ('Pastel','Churrasco','Picanha','Alcatra','Fraldinha','Costela','Maminha','Cupim','Cordeiro','Porco','Coca Zero','Frango','Coxinha de frango','Asa de frango','Coração de frango','Peito de frango','pao de alho','Pernil','Costelinha de porco')

for item in palavras:
    print(f'\nna Palavra {item} temos: ',end='')
    for vogal in item:
        if vogal.lower() in 'aeiou':
            print(f'{vogal.lower()}',end=' ')