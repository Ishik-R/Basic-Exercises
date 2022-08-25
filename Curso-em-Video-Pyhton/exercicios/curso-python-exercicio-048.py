# Exercício Python #048 - Soma ímpares múltiplos de três
# https://www.youtube.com/watch?v=iHjsUxNA-wo

# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('\n#048 - Soma dos ímpares múltiplos de três')
print('--' * 16)
r = 0
for c in range(3, 501, 6):
    r += c
print(f'A soma dos múltiplos de 3 entre 1 e 500 que não sejam pares é de {r}')