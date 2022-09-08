# Exercício Python #089 - Boletim com listas compostas
# https://www.youtube.com/watch?v=7xrCJnniqMw

# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#  No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

print("\n#089 - Boletim com listas compostas")
aluno = list()
classe = list()
while True:
    aluno.append(str(input("Nome: ")))
    aluno.append(float(input("Nota 1: ")))
    aluno.append(float(input("Nota 2: ")))
    classe.append(aluno[:])
    aluno.clear()
    cont = input("Aluno cadastrado com sucesso. Deseja continuar [S/N]? ").upper()
    if cont == 'N':
        break
print("=-" * 16)

print(f"{'N':<4} {'NOME:':<14} {'MÉDIA:':<5}")
print("--" * 16)
for i, aln in enumerate(classe):
    print(f"{i+1:<4} {aln[0]:<15} {(aln[1]+aln[2])/2:<4.1f}")

while True:
    print("--" * 16)
    ind = int(input("Mostrar notas de qual aluno (999 para encerrar)? "))
    while ind > len(classe) and ind != 999:
        ind = int(input("Valor inválido. Tente novamente (999 para encerrar): "))
    if ind == 999:
        break
    print(f"{ind} - {classe[ind-1][0]}: nota 1[{classe[ind-1][1]}]  nota 2[{classe[ind-1][2]}]")    