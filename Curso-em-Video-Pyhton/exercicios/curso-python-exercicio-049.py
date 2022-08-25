# Exercício Python #049 - Tabuada v.2.0
# https://www.youtube.com/watch?v=QtElJDa9ICM

# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
print('\n#049 - Tabuada v.2.0')
print('--' * 16)
num = int(input('Insira o valor para ver sua respectiva tabuada (até a décima multiplicação): '))
for x in range(1, 11):
    print(f'{x:2} x {num} = {x*num}')