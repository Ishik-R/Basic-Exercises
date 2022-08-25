# Exercício Python #051 - Progressão Aritmética
# https://www.youtube.com/watch?v=-OnqSGh0u4g

# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
#  No final, mostre os 10 primeiros termos dessa progressão.

print('\n#051 - Progressão Aritmética')
print('--' * 16)
print('Esta PA avançará até o décimo termo; insira abaixo o primeiro termo e a razão desejadas:')
a1 = float(input('a1 (primeiro termo): '))
r = float(input('r (razão): '))

print('\nEquação matemática:')
for n in range(1, 11):
    print(f'a{n} = {a1} + ({n} - 1) * {r} = {a1+(n-1)*r}')
    
print('\nExibição somente dos resultados:')
for n in range(1, 11):
    print(f'{a1+(n-1)*r} ', end = '→ ')
print('FIM\n')