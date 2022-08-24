# Exercício Python #039 - Alistamento Militar
# https://www.youtube.com/watch?v=ePwP4gU_waY

# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('\n#039 - Alistamento Militar')
print('--' * 16)
ano_nasc = int(input('Insira seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade > 18:
    print(f'Você terá {idade} anos no final deste ano.') 
    print(f'Você deveria ter se alistado em {ano_nasc+18}, {ano_atual-ano_nasc-18} ano(s) atrás.\n')
elif ano_atual - ano_nasc < 18:
    print(f'Você terá {idade} anos no final deste ano.')
    print(f'Você deverá ter se alistar em {ano_nasc+18}, daqui a {ano_nasc-ano_atual+18} ano(s).\n')
else:
    print(f'Você terá {idade} anos no final deste ano.')
    print(f'Você deverá ter se alistar em {ano_nasc+18}, ou seja, neste ano!\n')