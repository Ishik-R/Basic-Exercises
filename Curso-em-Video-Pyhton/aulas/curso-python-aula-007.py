# Curso Python #07 - Operadores Aritméticos
# https://www.youtube.com/watch?v=Vw6gLypRKmY

nome = input('Qual é o seu nome? ')
print('Seu nome e mais 20 espaços: {:20}!'.format(nome))
print('Seu nome e mais 20 espaços, mas alinhado à direita: {:>20}!'.format(nome))
print('Seu nome e mais 20 espaços, mas alinhado à esquerda: {:<20}!'.format(nome))
print('Seu nome centralizado entre os 20 espaços: {:^20}!'.format(nome))
print('Seu nome centralizado entre 20 sinais de igual: {:=^20}!'.format(nome))

print(f'Outro modo de utilizar o format, caro(a) {nome}.')

print('Vamos aos operadores aritiméticos: ')
n1 = int(input('Insira um valor inteiro: '))
n2 = int(input('Insira outro valor inteiro: '))
print(f'A soma vale {n1+n2}')
print(f'A subtração de {n1} por {n2} vale {n1-n2}')
print(f'O produto vale {n1*n2}')
print(f'A divisão de {n1} por {n2} vale {n1/n2:.3f} (arredondado para 3 casas depois da vírgula)')
print(f'A divisão inteira de {n1} por {n2} vale {n1//n2}')
print(f'A potência de {n1} elevado a {n2} vale {n1**n2}')

# A quebra de linha ocorre com \n
# A continuação de um print na mesma linha ocorre quando, no final de um print, inserimos ", end='' ", sendo que é possível inserir caracteres específicos
