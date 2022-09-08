# Exercício Python #090 - Dicionário em Python
# https://www.youtube.com/watch?v=HipQYUk4koA

# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#  No final, mostre o conteúdo da estrutura na tela.

print("\n#090 - Dicionário em Python")
print("--" * 16)

aluno = dict()
aluno['nome'] = str(input("Nome do aluno: "))
aluno['media'] = float(input(f"Média final para {aluno['nome']}: "))

if aluno['media'] >= 6:
    aluno['situacao'] = 'aprovado!'
elif aluno['media'] >= 4:
    aluno['situacao'] = 'em recuperação.'
else:
    aluno['situacao'] = 'reprovado.'

print("=-" * 16)
print(f" - Nome: {aluno['nome']}\n - Média final: {aluno['media']:.1f}\n - Situação: {aluno['situacao']}")