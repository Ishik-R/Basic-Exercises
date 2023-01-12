# Exercício Python #111 - Transformando módulos em pacotes
# https://www.youtube.com/watch?v=uBQ0--sRFUI
#
# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
#  Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
#   
#  **OBSERVAÇÃO**
#   A natureza deste exercício era de criar um pacote para armazenar as funções criadas pelo módulo 'moeda'.
#   Aqui é visível de que o simples ato de somente subir os arquivos dos programas criados no GitHub cria um problema.
#   Se os arquivos referentes ao exercício 111 forem reunidos e compilados, haverão erros.
#   O arquivo rodou corretamente com as devidas correções na organização dos diretórios e dos nomes dos arquivos.
#
#  APRESENTAÇÃO DA ORGANIZAÇÃO DOS DIRETÓRIOS:
#  ex111
#  |--curso-python-exercicio-111.py *O PRESENTE ARQUIVO
#  |--utilidadescev
#     |--__init__.py
#     |--dados 
#        |--__init__.py
#     |--moeda
#        |--__init__.py *AQUI SE ENCONTRAM TODAS AS FUNÇÕES PRESENTES NO 'moeda111'
#

print("\n#111 - Transformando módulos em pacotes")
print("--" * 16)

from ex111.utilidadescev import moeda
from ex111.utilidadescev import dados
 
p = float(input("Digite um valor em R$: "))
moeda.resumo(p,20,12)