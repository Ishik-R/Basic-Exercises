# Exercício Python #111 - Transformando módulos em pacotes
# https://www.youtube.com/watch?v=uBQ0--sRFUI

# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
#  Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
#
# **OBSERVAÇÃO**
#   Este arquivo na verdade é intitulado '__init__.py' e está localizado dentro do diretório 'moeda', dentro do pacote 'utilidadescev'
#   Para fins de exibição e organização na pasta de exercícios, já que não estou realizando-os com o devido versionamento,
#    o nome de exibição aparecerá como 'moeda111'.

def monetario(n):
    '''
    monetario(float n): esta função converte um valor float para uma apresentação visual de acordo com preços em reais (R$)
    :param n: valor de entrada a ser convertido.
    :return: a string contendo o mesmo valor, mas com uma vírgula no lugar do ponto, duas casas decimais e R$ antecedendo o valor.
    '''
    value = f'R${n:.2f}'.replace('.',',')
    return value

def aumentar(n,tax,change=True):
    '''
    aumentar(float n, float tax, bool change): esta função adiciona ao valor de entrada um respectivo valor em porcentagem.
     A saída também pode aparecer em uma apresentação visual de acordo com os preços em reais (R$).
    :param n: valor de entrada.
    :param tax: valor em porcentagem do aumento de n.
    :param change: indica se o valor a ser retornado deve ser formatado para a exibição monetária. Valor padrão: True.
    :return: o valor de n com uma adição percentual de tax%, podendo estar em um formato string para a exibição monetária.
    '''
    value =  n + (n*tax/100) 
    if change:
        value = f'R${value:.2f}'.replace('.',',')
    return value

def diminuir(n,tax,change=True):
    '''
    diminuir(float n, float tax, bool change): esta função subtrai ao valor de entrada um respectivo valor em porcentagem.
     A saída também pode aparecer em uma apresentação visual de acordo com os preços em reais (R$).
    :param n: valor de entrada.
    :param tax: valor em porcentagem da diminuição de n.
    :param change: indica se o valor a ser retornado deve ser formatado para a exibição monetária. Valor padrão: True.
    :return: o valor de n com uma redução percentual de tax%, podendo estar em um formato string para a exibição monetária.
    '''
    value = n - (n*tax/100)
    if change:
        value = f'R${value:.2f}'.replace('.',',')
    return value

def dobro(n,change=True):
    '''
    dobro(float n, bool change): esta função dobra o valor de entrada.
     A saída também pode aparecer em uma apresentação visual de acordo com os preços em reais (R$).
    :param n: valor de entrada.
    :param change: indica se o valor a ser retornado deve ser formatado para a exibição monetária. Valor padrão: True.
    :return: o valor de n multiplicado por 2, podendo estar em um formato string para a exibição monetária.
    '''
    value = 2*n
    if change:
        value = f'R${value:.2f}'.replace('.',',')
    return value

def metade(n,change=True):
    '''
    metade(float n, bool change): esta função divide o valor de entrada pela metade.
     A saída também pode aparecer em uma apresentação visual de acordo com os preços em reais (R$).
    :param n: valor de entrada.
    :param change: indica se o valor a ser retornado deve ser formatado para a exibição monetária. Valor padrão: True.
    :return: o valor de n divido por 2, podendo estar em um formato string para a exibição monetária.
    '''
    value = n/2 
    if change:
        value = f'R${value:.2f}'.replace('.',',')
    return value

def resumo(n, taxup=0, taxdown=0):
    '''
    resumo(float n, float taxup, float taxdown): esta função apresenta um resumo de todas as funções disponíveis no módulo 'moeda'.
    :param n: valor de entrada.
    :param taxup: indica o valor de aumento percentual do valor de entrada. Valor padrão: 0.
    :param taxdown: indica o valor de diminuição percentual do valor de entrada. Valor padrão: 0.
    :return: nulo. A função apenas imprime os resultados de 'aumentar', 'diminuir', 'dobro' e 'metade'.
    '''
    print("--"*16)
    print("RESUMO".center(30))
    print("--"*16)
    print(f"A metade de {monetario(n)}: \t{metade(n)}")
    print(f"O dobro de {monetario(n)}: \t{dobro(n)}")
    print(f"{taxup}% de aumento: \t{aumentar(n,taxup)}") 
    print(f"{taxdown}% de diminuição: \t{diminuir(n,taxdown)}") 
    print("-"*30)