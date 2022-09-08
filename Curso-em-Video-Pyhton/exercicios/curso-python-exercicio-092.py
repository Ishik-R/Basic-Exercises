# Exercício Python #092 - Cadastro de Trabalhador em Python
# https://www.youtube.com/watch?v=Vsqemzdrj78

# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#  Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#  Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

print("\n#092 - Cadastro de Trabalhador em Python")
print("--" * 16)

from datetime import date

dados = dict()
dados['nome'] = str(input("Nome: "))
dados['nascimento'] = int(input("Ano de nascimento: "))
dados['idade'] = date.today().year - dados['nascimento']

if dados['idade'] < 0:
    dados['invalid'] = True
elif dados['idade'] < 16:
    print("Você é considerado uma criança pelas leis, portanto, não deve possuir uma CTPS.")
    dados['crianca'] = True
else:
    dados['ctps'] = str(input("Carteira de Trabalho (digite 0 para indicar que não possui): "))
    if dados['ctps'] is not '0':
        dados['ano_contratacao'] = int(input("Ano de contratação: "))
        dados['salario'] = float(input('Salário: R$'))
        dados['idade_aposentadoria'] = dados['ano_contratacao']+35-dados['nascimento']

print("=-" * 16)
for key, info in dados.items():
    if key == 'invalid':
        print(f"Idade negativa. Tente novamente no ano de {dados['nascimento']}.")
        break
    if key == 'crianca':
        print("Por não poder oficialmente trabalhar, o cadastro está encerrado.")
        break

    if key == 'ctps':
        print(f"{key.upper()}: ", end="")
    else:
        print(f"{key.capitalize()}: ", end="")
    
    if key == 'idade' or key == 'idade_aposentadoria':
        print(f"{info} anos")
    elif key is 'salario':
        print(f"R${info:.2f}")
    else:
        print(f"{info}")