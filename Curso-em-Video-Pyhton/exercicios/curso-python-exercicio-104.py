# Exercício Python #104 - Validando entrada de dados em Python
# https://www.youtube.com/watch?v=VrQmMbPpbf0

# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
#  só que fazendo a validação para aceitar apenas um valor numérico.
#  Ex: n = leiaInt('Digite um n: ')
#
#  OBS: FUNCIONANDO APENAS PARA OS NÚMEROS QUE SÃO PURAMENTE NUMÉRICOS. NÚMEROS DECIMAIS E NEGATIVOS NÃO SÃO ACEITOS

print("\n#104 - Validando entrada de dados em Python")
print("--" * 16)

def leiaInt(msg):
    """
    -> leiaInt: esta função recebe uma entrada por parte do usuário e a retorna se o valor for um número inteiro.
     Enquanto o valor repassado não for um número inteiro a função deverá solicitar uma nova entrada.
    :param num: mensagem padrão de solicitação de entrada.
    :return: num, se num for um número inteiro. Caso contrário, a função deve solicitar uma nova entrada.
    """
    n = str(input(msg))
    while not n.isnumeric():
        print("ERRO! Digite um número inteiro válido.")
        n = str(input(msg))    
    return int(n)
    
#Programa principal:
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")