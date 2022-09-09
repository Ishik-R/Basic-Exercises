# Exercício Python #094 - Unindo dicionários e listas
# https://www.youtube.com/watch?v=ETnExBCFeps

# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#  No final, mostre: 
#    A) Quantas pessoas foram cadastradas
#    B) A média de idade
#    C) Uma lista com as mulheres
#    D) Uma lista de pessoas com idade acima da média

print("\n#094 - Unindo dicionários e listas")
print("--" * 16)

pessoas = list()
individuo = dict()
media = float(0)

while True:
    individuo['nome'] = str(input("Nome: "))
    individuo['sexo'] = str(input("Sexo [M/F]: ").upper())
    while individuo['sexo'] not in 'MF':
        individuo['sexo'] = str(input("ERRO! Por favor, digite M ou F: ").upper())
    individuo['idade'] = int(input("Idade: "))
    media += individuo['idade']
    pessoas.append(individuo.copy())
    
    confirm = str(input("Quer continuar [S/N]? ").upper())
    while confirm not in 'SN':
        confirm = str(input("ERRO! Por favor, digite S ou N: ").upper())
    if confirm == 'N':
        break     
media = media / len(pessoas)

print("-=" * 16)
mulheres = list()
maiores = list()
print(f"A) Número de pessoas cadastradas: {len(pessoas)} ")
print(f"B) Média de idade: {media:.2f} anos")
for p in pessoas:
    if p['sexo'] == 'F':
        mulheres.append(p['nome'])
    if p['idade'] > media:
        maiores.append(p['nome'])

print(f"C) Lista com os nomes das mulheres: {mulheres}")
print(f"D) Lista com os nomes das pessoas com a idade acima da média: {maiores}")