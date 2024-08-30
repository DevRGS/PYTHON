#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from time import sleep
from datetime import date

def voto(anoNascimento):
    anoAtual = date.today().year
    idade = anoAtual - anoNascimento

    if idade >= 18 and idade < 65:
        return f'Sua idade é {idade}, é OBRIGATÓRIO o VOTO'
    elif idade >= 16:
        return f'Sua idade é {idade}, é OPCIONAL o VOTO'
    else:
        return f'Sua idade é {idade}, NÃO PODE VOTAR'

anoNascimento = int(input('Digite seu ano de nascimento: '))
resultado = voto(anoNascimento)
print(resultado)

