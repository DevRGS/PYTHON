#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint

print("=-="*20)
print("JOKENPO DO RUIM")
print("=-="*20)
escolhas = ('Pedra', 'Papel','Tesoura')
pc = randint(0,2)

print("O Adversário PC já fez sua escolha! faça a sua!")
user = int(input("""Escolha entre:
          [ 0 ] Pedra
          [ 1 ] Papel
          [ 2 ] Tesoura
          
          Faça sua Escolha: """))

if user > 2:
    print("Escolhe uma opção válida mula, só tem 3 opção nesse caraio e ainda consegue errar, vai ser burro na casa do krl")  
elif pc == user:
     print("EMPATE! você jogou {} o PC também escolheu {}!".format(escolhas[user],escolhas[pc]))
elif pc == 0 and user == 1:
    print("Você Ganhou! jogou {} e o PC escolheu {}!".format(escolhas[user], escolhas[pc]))
elif pc == 1 and user == 2:
    print("Você Ganhou! jogou {} e o PC escolheu {}!".format(escolhas[user], escolhas[pc]))
elif pc == 2 and user == 0:
    print("Você Ganhou! jogou {} e o PC escolheu {}!".format(escolhas[user], escolhas[pc]))
else:
    print("Você Perdeu! jogou {} e o PC escolheu {}!".format(escolhas[user], escolhas[pc]))