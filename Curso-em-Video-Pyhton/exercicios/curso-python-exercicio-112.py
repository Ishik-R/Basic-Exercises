# Exercício Python #112 - Entrada de dados monetários
# https://www.youtube.com/watch?v=6vADeY5_pMs
#
# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
#  Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
#  mas com uma validação de dados para aceitar apenas valores que seja monetários.
#   
#  **OBSERVAÇÃO**
#   Este exercício depende da organização herdada do exercício 111, fazendo uso dos módulos 'moeda' e 'valor'.
#   O módulo 'dado' foi renomeado para 'valor112' e 'moeda' para 'moeda112' para fins de exibição no GitHub.
#   Aqui é visível de que o simples ato de somente subir os arquivos dos programas criados no GitHub cria um problema.
#   Se os arquivos referentes ao exercício 112 forem reunidos e compilados, haverão erros.
#
#  APRESENTAÇÃO DA ORGANIZAÇÃO DOS DIRETÓRIOS:
#  ex111
#  |--curso-python-exercicio-111.py *O PRESENTE ARQUIVO
#  |--utilidadescev
#     |--__init__.py
#     |--dados          *AQUI SE ENCONTRAM TODAS AS FUNÇÕES PRESENTES NO 'valor112'
#        |--__init__.py
#     |--moeda
#        |--__init__.py *AQUI SE ENCONTRAM TODAS AS FUNÇÕES PRESENTES NO 'moeda112'
#

print("\n#112 - Entrada de dados monetários")
print("--" * 16)

#VERSÃO COM OS DEVIDOS NOMES DOS MÓDULOS E PACOTES
#from ex111.utilidadescev import moeda
#from ex111.utilidadescev import dados
#
#p = dados.leia_dinheiro("Digite um valor em R$: "))
#moeda.resumo(p,20,12)

#VERSÃO COM OS NOMES DOS ARQUIVOS ENVIADOS AO GITHUB
import moeda112
import valor112

p = valor112.leia_dinheiro("Digite um valor em R$: ")
moeda112.resumo(p,20,12)