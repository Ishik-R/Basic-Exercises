# Exercício Python #057 - Validação de Dados
# https://www.youtube.com/watch?v=JGztEBLGj5E

# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
#  Caso esteja errado, peça a digitação novamente até ter um valor correto.

print("\n#057 - Validação de Dados")
print("--" * 16)

sexo = input("Informe o seu sexo [M/F]: ").upper().strip()

while sexo not in "MF":
    sexo = input("Entrada inválida, tente novamente. informe seu sexo [M/F]: ").upper().strip()
print(f"Informação registrada com sucesso. Sexo: {sexo}") 