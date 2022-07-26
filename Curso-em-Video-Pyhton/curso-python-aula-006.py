# Curso Python #06 - Tipos Primitivos e Saída de Dados
# https://www.youtube.com/watch?v=hdDHg1p3YVc

# Prática 1: verificação de o tipo primitivo de uma variável
n = input('Digite um valor: ')
print(type(n))

# Prática 2: soma entre dois valores inteiros
n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor: '))
s = n1 + n2
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))

# Prática 3: tipos primitivos
a = input('Digite algo: ')
print('O tipo de entrada padrão pelo input é String (str): {}'.format(type(a)))
print('Podemos verificar se a entrada é numérica: {}'.format(a.isnumeric()))
print('Podemos verificar se a entrada é alfabética: {}'.format(a.isalpha()))
print('Podemos verificar se a entrada é alfanumérica: {}'.format(a.isalnum()))