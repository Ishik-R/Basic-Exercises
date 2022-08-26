# Exercício Python #056 - Analisador completo
# https://www.youtube.com/watch?v=fokDF4th0IY

# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#  No final do programa, mostre: 
#  - a média de idade do grupo
#  - qual é o nome do homem mais velho
#  - quantas mulheres têm menos de 20 anos.

# OBSERVAÇÃO: provavelmente eu deveria ter feito este programa utilizando classes, mas ainda não entendi a estrutura geral da OOP em Python

print("\n#056 - Analisador completo")
print("--" * 16)

nomes = []
idades = []
sexos = []
idade_mais_velho = 0
nome_mais_velho = " "
mulheres_sub_20 = 0

print("Insira o nome, idade e sexo de 4 pessoas.")
for n in range(0, 4):
    print(f"\nPessoa {n+1}: ")
    nomes.insert(n, input("Nome: "))
    idades.insert(n, int(input("Idade: ")))
    sexos.insert(n, input("Sexo (M/F): ").upper())    
    if sexos[n] in "M" and idades[n] > idade_mais_velho:
        idade_mais_velho = idades[n]
        nome_mais_velho = nomes[n]
    if sexos[n] in "F" and idades[n] < 20:
        mulheres_sub_20 += 1

print(f"Média das idades: {sum(idades)/len(idades)}")
if nome_mais_velho != " ":
    print(f"Nome do homem mais velho do grupo: {nome_mais_velho}, com {idade_mais_velho}")
else:
    print("Nome do homem mais velho do grupo: não há homens neste grupo")
print(f"Mulheres abaixo de 20 anos: {mulheres_sub_20}\n")