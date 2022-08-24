# Exercício Python #044 - Gerenciador de Pagamentos
# https://www.youtube.com/watch?v=I-SH3QchuZ4

# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#  - à vista dinheiro/cheque: 10% de desconto
#  - à vista no cartão: 5% de desconto
#  - em até 2x no cartão: preço formal
#  - 3x ou mais no cartão: 20% de juros

print('\n#044 - Gerenciador de Pagamentos')
print('--' * 16)
valor = float(input('Total do preço das compras: R$ '))
print(f'''FORMAS DE PAGAMENTO:
[1] - à vista dinheiro/cheque: 10% de desconto
[2] - à vista no cartão: 5% de desconto
[3] - em até 2x no cartão: preço formal
[4] - 3x ou mais no cartão: 20% de juros''')
opt = input('Opção selecionada: ')

if opt == '1':
    print(f'Valor total a ser pago: R${valor*0.9:.2f} - 10% de desconto\n')
elif opt == '2':
    print(f'Valor total a ser pago: R${valor*0.95:.2f} - 5% de desconto\n')
elif opt == '3':
    print(f'Valor total a ser pago: R${valor:.2f} - preço formal\n')
elif opt == '4':
    print(f'Valor total a ser pago: R${valor*1.2:.2f} - 20% de juros\n')
else:
    print('Comando não compreendido. Desculpe.\n')