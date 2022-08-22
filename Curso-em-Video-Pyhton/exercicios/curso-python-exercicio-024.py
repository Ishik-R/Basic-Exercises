# Exercício Python #024 - Verificando as primeiras letras de um texto
# https://www.youtube.com/watch?v=QroT8cZMRnc

# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

print('\nEXERCÍCIO 024 - Verificando as primeiras letras de um texto')
print('--' * 16)

cidade = input('Onde você nasceu? ')
is_SANTO = cidade.lstrip().upper().split()[0]

if is_SANTO == 'SANTO':
    print('Sua cidade natal começa com Santo\n')
else: 
    print('Sua cidade natal não começa com Santo\n')
