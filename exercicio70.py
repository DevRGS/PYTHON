#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.

#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

soma = cont = 0
listagem = ('Mouse Pad', 70.85,
            'Teclado',99.85,
            'Mouse',400.99,
            'Monitor',650.55,
            'Placa Mãe X99',450.68,
            'Intel Xeon E5-2667 v4', 270.97,
            '4x Memória RAM 16GB', 400.97,
            'RX580 8GB', 567.55,
            'Fonte 500W', 420.43,
            'SSD 240GB', 124.45,
            'Water Cooler', 632.41,
            '8 Fans', 134.91)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
        cont += 1
    else:
        print(f'R${listagem[pos]:>7.2f}')
        soma += listagem[pos]
print('-'*40)
print(f'Foram {cont} itens, dando um custo total do Setup de: R${soma:.2f}')
