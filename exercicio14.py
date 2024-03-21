n1 = float(input('Digite o valor do seu sálario: '))
n2 = float(input('Digite quantos % você quer de aumento: '))

aumento = (n2/100) * n1
salario = n1+aumento

print('Parabéns! Você recebeu um aumento de R${:.2f}, agora seu novo sálario será R${:.2f}, a cerveja de hoje é por sua conta!'.format(aumento, salario))