#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
cores = {
    'limpa': '\033[m',
    'azul': '\033[0;34m',
    'red': '\033[0;31m',
    'destaque': '\033[7;30m',
    'amarelo': '\033[0;33m',
    'verde': '\033[0;32m'
}
print('\033[0;33m -*-'*10, '\033[m')
num = int(input('{}Digite {}qualquer {}número:{} '.format(
    cores['azul'], 
    cores['amarelo'],
    cores['red'], 
    cores['destaque'])))
print('\033[0;32m -*-'*10, '\033[m')

print('''Escolha uma Opção
      [ 1 ] Converter para Binário
      [ 2 ] Converter para Octal
      [ 3 ] Converter para Hexadecimal
      ''')
opcao = int(input('Sua Opção: '))

if opcao == 1:
    print('{}, em {}Binário{} fica: {}'.format(
        num, 
        cores['verde'],
        cores['limpa'], 
        bin(num)))

elif opcao == 2:
    print('{}, em {}Octal{} fica: {}'.format(
        num, 
        cores['verde'], 
        cores['limpa'], 
        oct(num)))
    
elif opcao == 3:
    print('{}, em {}Hexadecimal{} fica: {}'.format(
        num, 
        cores['verde'], 
        cores['limpa'], 
        hex(num)))

else:
    print('{}DIGITE UMA OPÇÃO VÁLIDA JÃO{}'.format(
        cores['red'],
        cores['limpa']))