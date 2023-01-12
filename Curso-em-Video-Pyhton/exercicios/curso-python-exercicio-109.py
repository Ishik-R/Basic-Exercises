# Exercício Python #109 - Formatando Moedas em Python
# https://www.youtube.com/watch?v=Y0zNYTHoGhQ

# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
#  informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
#
# OBS: a solução desenvolvida para o exercício 108 já estava adequada com a proposta deste exercício.
#  Como desenvolvimento extra, portanto, foi desenvolvida a documentação das funções do módulo 'moeda109'

print("\n#109 - Formatando Moedas em Python")
print("--" * 16)

import moeda109
 
p = float(input("Digite um valor em R$: "))
print(f"A metade de {moeda109.monetario(p)} é {moeda109.metade(p)}")
print(f"O dobro de {moeda109.monetario(p)} é {moeda109.dobro(p)}")
print(f"Aumentando nosso valor em 10% temos {moeda109.aumentar(p,10)}")