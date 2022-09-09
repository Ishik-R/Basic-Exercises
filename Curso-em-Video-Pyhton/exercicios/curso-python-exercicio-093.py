# Exercício Python #093 - Cadastro de Jogador de Futebol
# https://www.youtube.com/watch?v=5yKiud-YNaE

# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#  O programa vai ler o nome do jogador e quantas partidas ele jogou.
#  Depois vai ler a quantidade de gols feitos em cada partida.
#  No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

print("\n#093 - Cadastro de Jogador de Futebol")
print("--" * 16)

dados = dict()
gol = list()
dados['nome'] = str(input("Nome do jogador: "))
dados['atuacoes'] = int(input(f"Em quantos jogos {dados['nome']} atuou: "))

for n in range(0, dados['atuacoes']):
    gol.append(int(input(f"Jogo {n+1:<2} - gols: ")))
dados['gols'] = gol[:]
dados['total'] = sum(gol)

print("=-" * 16)
for key, value in dados.items():
    print(f"Dado: {key} - {value}")

print("=-" * 16)
print(f"{dados['nome']} atuou em {dados['atuacoes']} jogos, marcando um total de {dados['total']} gols.")
c = 1
for partida in dados['gols']:
    if partida == 1:
        print(f"  - jogo {c}: {partida} gol.")
    else:
        print(f"  - jogo {c}: {partida} gols.")
    c += 1