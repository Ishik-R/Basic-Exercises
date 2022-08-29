# Exercício Python #059 - Criando um Menu de Opções
# https://www.youtube.com/watch?v=OBJL5vPj4-E

# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#  [ 1 ] somar
#  [ 2 ] multiplicar
#  [ 3 ] maior
#  [ 4 ] novos números
#  [ 5 ] sair do programa
#  Seu programa deverá realizar a operação solicitada em cada caso.

print("\n#059 - Criando um Menu de Opções")
print("--" * 16)
print("Usuário, você deve inserir dois números e depois selecionar a opção desejada: ")
num1 = float(input("Insira o primeiro valor: "))
num2 = float(input("Insira o segundo valor: "))
print("""Usuário, as seguintes funções são disponibilizadas: 
 [ 1 ] somar
 [ 2 ] multiplicar
 [ 3 ] maior
 [ 4 ] novos números
 [ 5 ] sair do programa""")
opt = input("Escolha sua função: ")
while opt != "5":
    if opt == "1":
        print(f"SOMA: {num1} + {num2} = {num1+num2}")
    if opt == "2":
        print(f"MULTIPLICAÇÃO: {num1} * {num2} = {num1*num2}")
    if opt == "3":
        if num1 > num2:
            print(f"MAIOR NÚMERO: {num1} > {num2}")
        elif num1 < num2:
            print(f"MAIOR NÚMERO: {num1} < {num2}")
        else:
            print(f"MAIOR NÚMERO: {num1} = {num2}")
    if opt == "4":
        print("NOVOS NÚMEROS: por favor, insira os novos valores: ")
        num1 = float(input("Insira o primeiro valor: "))
        num2 = float(input("Insira o segundo valor: "))
    if opt not in '12345':
        print("Comando não reconhecido. Tente novamente.")
    print("""\nUsuário, qual sua próxima escolha? Opções: 
 [ 1 ] somar
 [ 2 ] multiplicar
 [ 3 ] maior
 [ 4 ] novos números
 [ 5 ] sair do programa""")
    opt = input("Escolha sua função: ")
print("Programa finalizado.")                    