 #Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
 
from datetime import date

cadastro = {}

cadastro['nome'] = str(input('Nome: '))
cadastro['ano'] = int(input('Ano de nascimento: '))
cadastro['ctps'] = int(input('Carteira de trabalho [0 se não tem]: '))

anoAtual = date.today().year
idade = anoAtual - cadastro['ano']
cadastro['idade'] = idade

if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Salário R$ '))
    
    anosContribuicao = 35
    anoAposentadoria = cadastro['contratacao'] + anosContribuicao
    idadeAposentadoria = idade + anosContribuicao
    
    cadastro['aposentadoria'] = anoAposentadoria
    
    print(f' - o nome é: {cadastro["nome"]}')
    print(f' - tem {cadastro["idade"]} anos')
    print(f' - a CTPS tem valor {cadastro["ctps"]}')
    print(f' - foi contratado no ano de {cadastro["contratacao"]}')
    print(f' - recebe o salário de R$ {cadastro["salario"]:.2f}')
    print(f' - irá se aposentar com {idadeAposentadoria} anos, no ano de: {cadastro["aposentadoria"]}')
else:
    print(f' - o nome é: {cadastro["nome"]}')
    print(f' - tem {cadastro["idade"]} anos')
    print(f' - a CTPS tem valor {cadastro["ctps"]}')


    





