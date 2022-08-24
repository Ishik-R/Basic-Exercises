# Python Exercício #041 - Classificando Atletas
# https://www.youtube.com/watch?v=ZiC5NgSGJXU

# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

# MATERIAL DE REFERÊNCIA: Obtenha o ano atual em Python
# https://www.delftstack.com/pt/howto/python/python-current-year/

from datetime import date

print('\n#041 - Classificando Atletas')
print('--' * 16)
birth_year = int(input('Insira seu ano de nascimento: '))
current_year = date.today().year
age = current_year - birth_year

if age < 0:
    print(f'Você possui {age} anos. Não temos categorias para idades negativas, desculpe.')
elif age <= 9:
    print(f'Você possui {age} anos. Categoria: MIRIM')
elif age <= 14:
    print(f'Você possui {age} anos. Categoria: INFANTIL')
elif age <=19:
    print(f'Você possui {age} anos. Categoria: JÚNIOR')
elif age <=25:
    print(f'Você possui {age} anos. Categoria: SÊNIOR')
else:
    print(f'Você possui {age} anos. Categoria: MASTER')