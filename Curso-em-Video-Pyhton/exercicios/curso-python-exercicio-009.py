# Exercício Python #009 - Tabuada
# https://www.youtube.com/watch?v=qajq3SI0QQs

x = int(input('Digite um valor para ver sua tabuada (até o décimo valor): '))
i = int(1)

print('--' * 12)
while i < 11:
    if i % 10 != 0:
        print(f' {i} x {x} = {i*x}')
    else:
        print(f'{i} x {x} = {i*x}')
    i += 1

print('--' * 12)
