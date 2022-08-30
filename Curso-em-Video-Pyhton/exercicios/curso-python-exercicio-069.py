# Exercício Python #069 - Análise de dados do grupo
# https://www.youtube.com/watch?v=4Ca6iRJo3M0

# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
#  A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#  No final, mostre:
#   A) quantas pessoas tem mais de 18 anos.
#   B) quantos homens foram cadastrados.
#   C) quantas mulheres tem menos de 20 anos. 

print("\n#069 - Análise de dados do grupo")
print("--" * 16)
age = []
sex = []
cond_a = 0
cond_b = 0
cond_c = 0
while True:
    age.append(int(input("Idade: ")))
    sex.append(str(input("Sexo [M/F]: ").upper().strip()))
    if age[-1] >= 18:
        cond_a += 1
    if sex[-1] in 'M':
        cond_b += 1
    if age[-1] < 18 and sex[-1] in 'F':
        cond_c += 1    
    opt = input("Você quer continuar? [S/N] ").upper().strip()
    while opt not in 'SN':
        print("Entrada inválida. Tente novamente.")
        opt = input("Você quer continuar? [S/N] ").upper().strip()
    print("=-" * 16)
    if opt == 'N':
        break
print(f"Pessoas com mais de 18 anos: {cond_a}")
print(f"Quantos homens foram cadastrados: {cond_b}")
print(f"Quantas mulheres tem menos de 20 anos: {cond_c}")
print("=-" * 16)