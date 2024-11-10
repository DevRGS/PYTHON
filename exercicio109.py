from exercicio109.lib.interface import *
from exercicio109.lib.arquivo import *
from time import sleep

arq = 'exercicio109\\lib\\arquivo\\cursoemvideo.txt'

if not arquivoExiste(arq):  
    criarArquivo(arq)

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
        
        
        