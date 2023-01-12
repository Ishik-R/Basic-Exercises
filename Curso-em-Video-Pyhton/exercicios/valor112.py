# Exercício Python #112 - Entrada de dados monetários
# https://www.youtube.com/watch?v=6vADeY5_pMs
#
# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
#  Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
#  mas com uma validação de dados para aceitar apenas valores que seja monetários.
#
# **OBSERVAÇÃO**
#   Este arquivo na verdade é intitulado '__init__.py' e está localizado dentro do diretório 'dados', dentro do pacote 'utilidadescev'
#   Para fins de exibição e organização na pasta de exercícios, já que não estou realizando-os com o devido versionamento,
#    o nome de exibição aparecerá como 'valor112'.

def leia_dinheiro(msg):
    while True:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha():
            print(f"{entrada} é inválida! Por favor, tente novamente.")
        else:
            return float(entrada)