# Exercício Python #109 - Formatando Moedas em Python
# https://www.youtube.com/watch?v=Y0zNYTHoGhQ

# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
#  informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

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
