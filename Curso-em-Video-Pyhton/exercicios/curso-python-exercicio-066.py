# Exercício Python #066 - Vários números com flag
# https://www.youtube.com/watch?v=d2ug6quC1bk

# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
#  O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#  No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

print("\n#066 - Vários números com flag")
print("--" * 16)
count = 0
list_num = []
print("Insira quantos números inteiros você quiser. 999 interrompe a execução.")
while True: 
    list_num.append(int(input("Insira um número inteiro: ")))
    if list_num[-1] == 999:
        break
    else:
        count += 1
if count == 1:
    print(f"\nFoi inserido {count} valor.")
else:
    print(f"\nForam inseridos {count} valores.")
print(f"Soma dos valores: {sum(list_num)}")