#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

from utilidadesCev import moeda
from utilidadesCev import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 35, 20)