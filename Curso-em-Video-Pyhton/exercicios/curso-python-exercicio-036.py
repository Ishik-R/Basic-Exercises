# Exercício Python #036 - Aprovando Empréstimo
# https://www.youtube.com/watch?v=IV13X0QOMU8

# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#  Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#  A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('\n#036 - Aprovando Empréstimo')
print('--' * 16)
print(f'Observação: a prestação mensal não deve exceder 30% do salário do comprador')
casa = float(input('Qual o valor da casa (em R$)? '))
anos = int(input('Em quantos anos o comprador pretende quitar a casa? '))
salario = float(input('Qual o salário do comprador (em R$)? '))

prestacao = casa/(anos*12)
if prestacao > 0.3*salario:
    print(f'\nEste empréstimo não pode ser concedido! A prestação mensal prevista de R${prestacao:.2f} ultrapassa 30% de seu salário.')
else:
    print(f'\nEmpréstimo aprovado! A prestação mensal (sem juros) está prevista em R${prestacao:.2f}')