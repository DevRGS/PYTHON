#Transformando pacotes em módulos

from utilidadesCev.moeda import resumo as rs

num = float(input('Digite um valor em R$: '))
aumento = int(input('Quanto quer aumentar: '))
reducao = int(input('Quanto quer reduzir: '))

rs(num, aumento, reducao)