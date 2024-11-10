def tabelaMulti(num, table=1):
    for c in range(1, table+1):
        print(f'{num} * {c} = {num * c}')
    print('FIM')

def aumentaDez(num, f = True):
    num = num * 1.1
    if f == True:
        return f'R$ {num:.2f}'.replace('.',',')
    else: return f'{num:.2f}'


def menosDez(num, f = True):
    num = num * 0.9
    if f == True:
        return f'R$ {num:.2f}'.replace('.',',')
    else: return f'{num:.2f}'


def dobro(num, f = True):
    num = num * 2
    if f == True:
        return f'R$ {num:.2f}'.replace('.',',')
    else: return f'{num:.2f}'


def metade(num, f = True):
    num = num / 2
    if f == True:
        return f'R$ {num:.2f}'.replace('.',',')
    else: return f'{num:.2f}'
    

def resumo(num, aumento, reducao):
    titulo = 'ANALISE DO VALOR'.center(40)
    
    linha = '-' * len(titulo)
    valorComAumento = num + (num * (aumento / 100))
    valorComReducao = num - (num * (reducao / 100))
    dobro = num * 2
    metade = num / 2
    
    print(linha)
    print(titulo)
    print(linha)
    
    print(f"{'O Valor analisado:'.ljust(30)}{f'R$ {num:.2f}'.rjust(10).replace('.',',')}")
    print(f"{'O Dobro do Valor:'.ljust(30)}{f'R$ {dobro:.2f}'.rjust(10).replace('.',',')}")
    print(f"{'A Metade do Valor:'.ljust(30)}{f'R$ {metade:.2f}'.rjust(10).replace('.',',')}")
    print(f"{f'Com o aumento de {aumento}%:'.ljust(30)}{f'R$ {valorComAumento:.2f}'.rjust(10).replace('.',',')}")
    print(f"{f'Com a redução de {reducao}%'.ljust(30)}{f'R$ {valorComReducao:.2f}'.rjust(10).replace('.',',')}")
