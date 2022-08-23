# Curso Python #012 - Condições Aninhadas
# https://www.youtube.com/watch?v=j9bYDjaAYzw

print("\nAULA 012 - Condições Aninhadas")
print("--" * 16)

# Essencialmente, esta é uma aula que descreve a funcionalidade do elif 

fatia = float(input("Quantos pedaços de pizza você consegue comer em uma refeição? "))

if fatia == 0:
    print("Nossa, você não gosta de pizza?")
elif fatia < 3 and fatia > 0:
    print("Bem, você parece ser uma pessoa com apetite normal.")
elif fatia == 3:
    print("Nossa, que apetite!")
elif fatia > 3:
    print("Você tem um baita apetite!")
else:
    print("Desculpe, não existem pizzas negativas.")