#pessoas = {
#    'nome': 'Gustavo',
#    'sexo': 'M',
#    'idade': 22
#    }
#
#print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos, e é do sexo {pessoas["sexo"]}')

##print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#
#for k in pessoas.values():
#    print(k)
#    
#for k in pessoas.keys():
#    print(k)
#    
#del pessoas['idade']
#
#pessoas['nome'] = 'Rafael'
#
#pessoas['peso'] = 85.5
#
#for k, v in pessoas.items():
#    print(f'o {k} = {v}')
#    
# Vamos criar um dicionário dentro de uma lista.
#
#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'PR'}
#
#brasil.append(estado1)
#brasil.append(estado2)
#
#print(estado1)
#print(brasil[0])
#print(brasil[0]['uf'])
#

estado = dict()
brasil = list()

for c in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)

#for e in brasil:
#    for k, v in e.items():
#        print(f'O campo {k} tem valor {v}')
#        
#for e in brasil:
#    for v in e.values():
#        print(v)
#        
#for e in brasil:
#    for v in e.values():
#        print(v, end=' ')
#        