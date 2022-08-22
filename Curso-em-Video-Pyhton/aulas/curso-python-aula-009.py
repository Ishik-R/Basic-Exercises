# Curso Python #09 - Manipulando Texto
# https://www.youtube.com/watch?v=a7DH88vk2Sk

print('\nAULA 009 - Manipulação de Texto')
print('--' * 16)

frase = 'Temos aqui uma Frase de exemplo'
print(f'\n{frase}')
print('\nFATIAMENTO')
print(f'Podemos selecionar um elemento de uma string, indicando seu índice: {frase[6]}')
print(f'Podemos selecionar um intervalo de elementos: {frase[6:10]}')
print(f'Podemos especificar a quantidade de índices ue devemos pular ao percorrer uma string: {frase[6:20:2]}')
print(f'Podemos determinar a exibição dos elementos até um determinado índice: {frase[:10]}')
print(f'Podemos determinar a exibição dos elementos a partir de um determinado índice: {frase[11:]}')

print('\nANÁLISE')
print(f'Função para verificação do tamanho de uma string: lenght - {len(frase)}')
print('Função para contagem de elementos presentes em uma string (no caso, a letra e): count -', frase.count('e'))
print('É possível utilizar o count em um intervalo pré-determinado. Aparições da letra a entre o índice 0 e 10:', frase.count('a',0,10))
print('Podemos procurar por um conjunto específicos de caracteres na string (no caso, a sílaba ma) - find:', frase.find('ma'))
print('Podemos verificar a existência ou não de um conjunto específico de caracteres (no caso, texto) - in: ', 'texto' in frase)

print('\nMANIPULAÇÃO')
print('A substituição de elementos pode ocorrer por meio da função replace:', frase.replace('Frase','oração'))
print('Tornar todos os caracteres maiúsculos - função upper:', frase.upper())
print('Tornar todos os caracteres minúsculos - função lower:', frase.lower())
print('Transformar a primeira letra da string em uma maiúscula - função capitalize:', frase.capitalize())
print('Transformar todas as primeiras letras de cada palavra em uma maiúscula - função title:', frase.title())
print('Remoção de espaços redundantes no começo e no final de uma string - função strip:', frase.strip())
print('Remoção de espaços redundantes na direita de uma string - função rstrip:', frase.rstrip())
print('Remoção de espaços redundantes na esquerda de uma string - função lstrip:', frase.lstrip())
print('Separação da string em uma lista de palavras - função split:', frase.split())
print('Junção dos elementos de uma lista - função join:', '-'.join(frase))