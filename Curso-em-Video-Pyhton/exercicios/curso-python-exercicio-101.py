# Exercício Python #101 - Funções para votação
# https://www.youtube.com/watch?v=czDcimdc3GU

# Exercício Python 101: Crie um programa que tenha uma função chamada voto()
#  que vai receber como parâmetro o ano de nascimento de uma pessoa,
#  retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

print("\n#101 - Funções para votação")
print("--" * 16)

def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f"Você possui ou possuirá {idade} anos neste ano. Voto NEGADO"
    elif idade <= 18 or idade > 65:
        return f"Você possui ou possuirá {idade} anos neste ano. Voto OPCIONAL"
    else: 
        return f"Você possui ou possuirá {idade} anos neste ano. Voto OBRIGATÓRIO" 

ano = int(input("Em que ano você nasceu? "))
print(voto(ano))
