n1 = float(input('Digite o valor do Produto: '))
n2 = float(input('Digite quantos % de Desconto você quer: '))

desc = (n2/100) * n1
novo = n1-desc

print('Você terá um desconto de R${:.2f}, logo o valor total de seu produto é: R${:.2f}'.format(desc, novo))

