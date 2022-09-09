# Exercício Python #095 - Aprimorando os Dicionários
# https://www.youtube.com/watch?v=mw1So0r317Y

# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

print("\n#095 - Aprimorando os Dicionários")
print("--" * 16)

jogador = dict()
players = list()
gol = list()

while True:
    jogador['nome'] = str(input("Nome do jogador: "))
    jogador['atuacoes'] = int(input(f"Em quantos jogos {jogador['nome']} atuou: "))
    for n in range(0, jogador['atuacoes']):
        gol.append(int(input(f"Jogo {n+1:<2} - gols: ")))
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    players.append(jogador.copy())
    jogador.clear()
    gol.clear()

    opt = str(input("Você quer inserir os jogador de outro jogador [S/N]? ").upper())
    while opt not in 'SN':
        opt = str(input("ENTRADA INVÁLIDA! Escolha entre S ou N: ").upper())
    if opt == 'N':
        break

print("=-" * 16)
for c, p in enumerate(players):
    print(f"CÓDIGO: {c} - {p['nome']}") 
    print(f" HISTÓRICO DAS {p['atuacoes']} ATUAÇÕES: - {p['gols']} - TOTAL: {p['total']}\n")

while True:
    print("=-" * 16)
    opt = int(input("Mostrar dados - selecione o código do jogador (999 para parar): "))
    if opt == 999:
        break
    else:
        print(f"* LEVANTAMENTO: {players[opt]['nome']}")
        for c, partida in enumerate(players[opt]['gols']):
            if partida <= 1:
                print(f"  - jogo {c}: {partida} gol.")
            else:
                print(f"  - jogo {c}: {partida} gols.")