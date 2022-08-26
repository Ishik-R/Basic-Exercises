# Exercício Python #054 - Grupo da Maioridade
# https://www.youtube.com/watch?v=IL5iBWoKRIs

# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. 
#  No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

print('\n#054 - Grupo da Maioridade')
print('--' * 16)

pessoas = []
maior = 0
menor = 0
print("Insira a data de nascimento de 7 pessoas:")
for n in range(0, 7):
    pessoas.insert(n, int(input(f"Pessoa {n+1}: ")))
    if date.today().year-pessoas[n] > 17:
        maior += 1
    else:
        menor += 1

print(f"No total, temos {maior} pessoa(s) maiores de idade e {menor} pessoas menores de idade.")