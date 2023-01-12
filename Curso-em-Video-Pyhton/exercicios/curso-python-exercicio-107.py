# Exercício Python #107 - Exercitando módulos em Python
# https://www.youtube.com/watch?v=y8pI8YBphQI

#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas:
#  - aumentar()
#  - diminuir()
#  - dobro()
#  - metade()
#  Faça também um programa que importe esse módulo e use algumas dessas funções.

print("\n#107 - Exercitando módulos em Python")
print("--" * 16)

import moeda

p = float(input("Digite um valor em R$: "))
print(f"A metade de R${p} é R${moeda.metade(p)}")
print(f"O dobro de R${p} é R${moeda.dobro(p)}")
print(f"Aumentando nosso valor em 10%, temos R${moeda.aumentar(p,10)}")