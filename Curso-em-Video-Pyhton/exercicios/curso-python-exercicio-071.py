# Exercício Python #071 - Simulador de Caixa Eletrônico
# https://www.youtube.com/watch?v=_XGgwltYpYk

# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
#  No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro).
#  O programa vai informar quantas cédulas de cada valor serão entregues.
#  OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("\n#071 - Simulador de Caixa Eletrônico")
print("--" * 16)
title = "CAIXA ELETRÔNICO"
print(title.center(32))
print("--" * 16)
n1 = 0
n10 = 0
n20 = 0
n50 = 0
withdraw = int(input("Qual é o valor que você quer sacar? R$ ")) 
while withdraw/50 > 0 and withdraw-50 >= 0: 
    withdraw -= 50
    n50 += 1
while withdraw/20 > 0 and withdraw-20 >= 0:
    withdraw -= 20
    n20 += 1
while withdraw/10 > 0 and withdraw-10 >= 0:
    withdraw -= 10
    n10 += 1   
while withdraw != 0:
    withdraw -= 1
    n1 += 1          
if n50 > 1:
    print(f"Total de {n50} cédulas de R$50")
elif n50 == 1:
    print(f"Total de {n50} cédula de R$50")
if n20 > 1:
    print(f"Total de {n20} cédulas de R$20")
elif n20 == 1:
    print(f"Total de {n20} cédula de R$20")
if n10 > 1:
    print(f"Total de {n10} cédulas de R$10")
elif n10 == 1:
    print(f"Total de {n10} cédula de R$10")
if n1 > 1:
    print(f"Total de {n1} cédulas de R$1")
elif n1 == 1:
    print(f"Total de {n1} cédula de R$1")                 