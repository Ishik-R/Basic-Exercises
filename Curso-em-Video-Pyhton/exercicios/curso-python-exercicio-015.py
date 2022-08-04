# Exercício Python #015 - Aluguel de Carros
# https://www.youtube.com/watch?v=I4NYUeetLAc

# Enunciado: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('\nCALCULADORA DE ALUGUEL DE CARROS')
print('--' * 12)
d = int(input('Por quantos dias o carro foi alugado? '))
km = int(input('Quantos kilômetros foram percorridos com o carro? '))
print(f'O total a ser pago é de R${d*60+km*0.15:.2f}.\n')