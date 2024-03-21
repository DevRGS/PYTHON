# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
cores = {
    'limpa': '\033[m',
    'azul': '\033[0;34m',
    'red': '\033[0;31m',
    'destaque': '\033[7;30m',
    'amarelo': '\033[0;33m',
    'verde': '\033[0;32m'
}

print('\033[0;33m -*-'*10, '\033[m')
print('{} EMPRESTIMO{} CONSIGNADO {}!!!'.format(
    cores['amarelo'], 
    cores['red'], 
    cores['azul']))
print('\033[0;32m -*-'*10, '\033[m')

casa = float(input('Digite o valor da casa que deseja: '))
salario = float(input('Digite seu salário BRUTO: '))
prestacao = int(input('Em quantos anos quer pagar: '))

parcialSal = salario * 0.3
valorPrest = casa / (prestacao * 12)

if valorPrest <= parcialSal:
    print('{}Excelente!{}, Seu {}Emprestimo{} esta {}APROVADO{}!!!'.format(
    cores['amarelo'],
                                                                           cores['limpa'],
                                                                           cores['verde'],
                                                                           cores['limpa'],
                                                                           cores['azul'],
                                                                           cores['limpa']))
else:
    print('Valor muito {}ALTO{} meu chapa, tive que {}Negar{} seu {}Emprestimo'.format(
    cores['red'],
                                                                            cores['limpa'],
                                                                            cores['amarelo'],
                                                                            cores['limpa'],
                                                                            cores['red']))
