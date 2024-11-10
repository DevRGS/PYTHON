from programas_uteis import numeros

numb = float(input("Digite um número em R$: "))
formatado = int(input("Quer os valores formatados? [1 = SIM / 0 = NÃO]: "))
if formatado == 1:
    formatado = True
else:
    formatado = False

print(f"o valor de {numb} mais 10% é: {numeros.aumentaDez(numb, formatado)}")
print(f"o valor de {numb} menos 10% é: {numeros.menosDez(numb, formatado)}")
print(f"o valor do dobro de {numb} é: {numeros.dobro(numb, formatado)}")
print(f"o valor da metade de {numb} é: {numeros.metade(numb, formatado)}")
