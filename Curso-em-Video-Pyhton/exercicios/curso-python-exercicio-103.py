# Exercício Python #103 - Ficha do Jogador
# https://www.youtube.com/watch?v=FbOvilKfHMI

# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
#  o nome de um jogador e quantos gols ele marcou.
#  O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

print("\n#103 - Ficha do Jogador")
print("--" * 16)

def ficha(nome,gol):
    """
    -> ficha: recebe os parâmetros do nome de um jogador e quantos gols ele marcou, exibindo-os. 
        Se os valores não forem devidamente informados, a função deve exibir os valores padrões.
    :param nome: recebe o nome do jogador. Valor padrão: <desconhecido>
    :param gol: recebe o número de gols marcados. Admite somente valores naturais. Valor padrão: 0
    :return: nenhum retorno. Somente exibe a mensagem apresentando a ficha do jogador.
    """
    if nome.strip()=='':
        nome="<desconhecido>"
    print(f"O jogador {nome} fez ", end="")

    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    if gol < 0:
        print("um valor inválido de gols no campeonato.")
    elif gol==1:
        print(f"{gol} gol no campeonato")
    else:
        print(f"{gol} gols no campeonato.")
    
nome = str(input("Nome do jogador: "))
gols = str(input("Número de gols: "))
ficha(nome, gols)