#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
from utilidadesCev.dado import (leiaIntTry,leiaFloat)

n1 = leiaIntTry('Digite um valor: ')
n2 = leiaFloat('Digite um Real: ')

print(f'o valor inteiro foi {n1} e o real foi {n2}')
