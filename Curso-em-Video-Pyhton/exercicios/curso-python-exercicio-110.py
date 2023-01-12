# Exercício Python #110 - Reduzindo ainda mais seu programa
# https://www.youtube.com/watch?v=1Ks218WINT8

# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
#  que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

print("\n#110 - Reduzindo ainda mais seu programa")
print("--" * 16)

import moeda110
 
p = float(input("Digite um valor em R$: "))
moeda110.resumo(p,20,12)