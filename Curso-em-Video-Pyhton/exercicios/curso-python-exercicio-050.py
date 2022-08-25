# Exercício Python #050 - Soma dos pares
# https://www.youtube.com/watch?v=rJaBLOW57Jg

# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
#  Se o valor digitado for ímpar, desconsidere-o.

print('\n#050 - Soma dos pares')
print('--' * 16)

c = 0
r = 0
for x in range(0, 6):
    num = int(input(f'Valor {x+1}: '))
    if num % 2 == 0:
        c += 1
        r += num
print(f'Números contabilizdos. Você inseriu {c} número(s) par(es), cuja soma total vale {r}')