# Exercício Python #034 - Aumentos múltiplos
# https://www.youtube.com/watch?v=Sfadj_AzKHw

# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#  Para salários superiores a R$1250,00, calcule um aumento de 10%.
#  Para os inferiores ou iguais, o aumento é de 15%.
print("\n#034 - Aumentos múltiplos")
print("--" * 16)

sal = float(input("Insira o valor do salário de um funcionário (em R$) para calcularmos seu aumento: "))

if sal <= 1250:
    print(f"O novo salário será de R${sal*1.15:.2f}")
else:
    print(f"O novo salário será de R${sal*1.10:.2f}")