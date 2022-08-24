# Exercício Python #043 - Índice de Massa Corporal
# https://www.youtube.com/watch?v=b7r34za963I

# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#  - IMC abaixo de 18,5: Abaixo do Peso
#  - Entre 18,5 e 25: Peso Ideal
#  - 25 até 30: Sobrepeso
#  - 30 até 40: Obesidade
#  - Acima de 40: Obesidade Mórbida

# MATERIAL DE REFERÊNCIA: Dicas em Saúde - Obesidade
# https://bvsms.saude.gov.br/bvs/dicas/215_obesidade.html

print('\n#043 - Índice de Massa Corporal')
print('--' * 16)
peso = float(input('Qual é o seu peso (em kg)? '))
altura = float(input('Qual é a sua altura (em m)? '))
imc = peso / altura**2

if imc < 18.5:
    print(f'IMC abaixo de 18.5: {imc:.1f} - Abaixo do Peso')
elif imc <= 25:
    print(f'IMC de 18.5 até 25: {imc:.1f} - Peso Ideal')
elif imc <= 30:
    print(f'IMC de 25 até 30: {imc:.1f} - Sobrepeso')
elif imc <= 40:
    print(f'IMC de 30 até 40: {imc:.1f} - Obesidade')
else:
    print(f'IMC acima de 40: {imc:.1f} - Obesidade Mórbida')            