#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expre = str(input('Digite uma expressão: '))
a = (expre.count(')'))
b = (expre.count('('))
c = (a + b)
if c % 2 == 0:
    print('Esta é uma expressão válida')
else:
    print('Esta não é uma expressão válida')

 