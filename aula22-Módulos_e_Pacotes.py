import prog_uteis as pu

while True:
    num = int(input('Digite um número para ver seu fatorial: '))
    fat = pu.fatorial(num)
    print(f'O valor fatorial de {num} é {fat}')
    resp =(input(f'Quer ver outro fatorial? [S/N] '))
    if resp in 'nN':
        break