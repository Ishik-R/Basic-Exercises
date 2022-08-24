# Exercício Python #037 - Conversor de Bases Numéricas
# https://www.youtube.com/watch?v=B3F0IjH5WAM

# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#  1 para binário, 2 para octal e 3 para hexadecimal.

print('\n#037 - Conversor de Bases Numéricas')
print('--' * 16)
num = int(input('Digite o valor inteiro a ser convertido: '))
print('''Escolha a base para conversão:
    [1] para binário 
    [2] para octal 
    [3] para hexadecimal ''')
opt = input('Sua opção: ')

if opt == '1':
    print(f'{num} convertido para binário: {bin(num)[2:]}')
elif opt == '2':
    print(f'{num} convertido para octal: {oct(num)[2:]}')
elif opt == '3':
    print(f'{num} convertido para hexadecimal: {hex(num)[2:]}')
else:
    print('Desculpe, não entendi o comando. Tente novamente.')