#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#
#– à vista dinheiro/cheque: 10% de desconto
#
#– à vista no cartão: 5% de desconto
#
#– em até 2x no cartão: preço formal 
#
#– 3x ou mais no cartão: 20% de juros

prod = float(input("Digite o valor do produto: "))
formPag = int(input("""Formas de pagamento: 
                    [ 1 ] COMO É AMIGO?
                    [ 2 ] DÉBITO Á VISTA
                    [ 3 ] CRÉDITO
                    
                    Escolha uma Opção: """))

if formPag == 1:
   valor = prod - (prod * 0.1)
   print("Você Ganhou um descontinho bão, tu vai paga R${}".format(valor))
elif formPag == 2:
    valor = prod - (prod*0.05)
    print("Você Ganhou um desconto, o valor total fica em R${}".format(valor))
elif formPag == 3:
    parcela = int(input("""Em quantas vezes quer fazer?
                        [ 1x ]
                        [ 2x ]
                        [ 3x ]
                        [ 4x ]
                        [ 5x ]
                        
                        Escolha uma opção: """))
    if parcela > 2:
        valor = prod + (prod * 0.2)
        print("TA BÃO, TU VAI PAGAR {}x de R${:.2f}".format(parcela, prod/parcela))
        print("O VALOR TOTAL FICA EM R${}".format(valor))
    else:
        print("PELO MENOS NÃO É PARCELADO! O VALOR TOTAL FICA EM R${}".format(prod))

else:
    print("VAI SER MULA NO KRL, SÓ TEM 3 OPÇÃO E TU CONSEGUE ERRAR VEI, VSF")