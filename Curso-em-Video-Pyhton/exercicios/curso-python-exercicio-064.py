# Exercício Python #064 - Tratando vários valores v1.0
# https://www.youtube.com/watch?v=mYlbttiLHM0

# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
#  O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#  No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print("\n#064 - Tratando vários valores v1.0")
print("--" * 16)
n = int(input("Digite um número inteiro (999 para parar): "))
soma = 0
c = 0
while n != 999: 
    soma += n
    c+=1
    n = int(input(f"Digite um número inteiro (999 para parar): "))
print(f"Foram digitados {c} números, e a soma total entre eles é de {soma}")