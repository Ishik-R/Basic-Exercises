# Exercício Python #008 - Conversor de Medidas
# https://www.youtube.com/watch?v=KjcdG05EAZc

n = float(input('Insira um valor em metros: '))
print(f'A medida de {n:.1f}m corresponde a:')
print(f'{n/1000}km \n{n/100}hm \n{n/10}dam \n{n}m')
print(f'{n*10:.0f}dm \n{n*100:.0f}cm \n{n*1000:.0f}mm')