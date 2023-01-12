#  Python #108 - Formatando Moedas em Python
# https://www.youtube.com/watch?v=KtRkGEeUdqE

# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda()
#  que consiga mostrar os números como um valor monetário formatado.

print("\n#108 - Formatando Moedas em Python")
print("--" * 16)

import moeda108
 
p = float(input("Digite um valor em R$: "))
print(f"A metade de {moeda108.monetario(p)} é {moeda108.metade(p)}")
print(f"O dobro de {moeda108.monetario(p)} é {moeda108.dobro(p)}")
print(f"Aumentando nosso valor em 10% temos {moeda108.aumentar(p,10)}")