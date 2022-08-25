# Exercício Python #052 - Números primos
# https://www.youtube.com/watch?v=Er5Hyd4LyVw

# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('\n#052 - Números primos')
print('--' * 16)

num = int(input('Insira um valor inteiro para analisarmos se ele é primo: '))
c = 0

for x in range(1, num+1):
    if(num % x == 0):
        c += 1
        print(f'\033[4;35m{x}\033[m', end=' ')
    else:
        print(f'{x}', end=' ')

if(c > 2):
    print(f'\n{num} é divisível por {c} números menores que ele, portanto, ele não é primo.')
else:
    print(f'\n{num} é divisível por apenas {c} números menores que ele: 1 e ele próprio, portanto, {num} é primo.')