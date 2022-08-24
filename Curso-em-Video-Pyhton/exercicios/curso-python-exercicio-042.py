# Exercício Python #042 - Analisando Triângulos v2.0
# https://www.youtube.com/watch?v=ZX7sCPjcHA0

# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#  - EQUILÁTERO: todos os lados iguais
#  - ISÓSCELES: dois lados iguais, um diferente
#  - ESCALENO: todos os lados diferentes

print('\n#042 - Analisando Triângulos v2.0')
print('--' * 16)
print("Insira o valor de três segmentos de reta para verificarmos se é possível construir um triângulo com elas.")
l1 = float(input('Valor 1: '))
l2 = float(input('Valor 2: '))
l3 = float(input('Valor 3: '))

if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('Estes segmentos de reta conseguem formar um triângulo.')
    if l1==l2 and l2==l3:
        print('Tipo de triãngulo: EQUILÁTERO')
    elif l1!=l2 and l2!=l3:
        print('Tipo de triângulo: ESCALENO')
    else:
        print('Tipo de triângulo: ISÓCELES')
else:
    print('Estes segmentos de reta não conseguem formar um triângulo.')