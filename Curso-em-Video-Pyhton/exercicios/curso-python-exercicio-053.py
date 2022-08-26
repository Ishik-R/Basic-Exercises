# Exercício Python #053 - Detector de Palíndromo
# https://www.youtube.com/watch?v=5VBWe6BXzRo&t=1s

# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

print('\n#053 - Detector de Palíndromo')
print('--' * 16)

frase = input('Digite sua frase: ')
frase_mod = frase.upper().replace(" ","")
print(f'\nA frase inserida foi: {frase}')
print(f'Ao desconsiderar os espaços, ela se torna: {frase_mod}')
if frase_mod == frase_mod[::-1]:
    print(f'Esta frase invertida é um palíndromo: {frase_mod[::-1]}\n')
else:
    print(f'Esta frase invertida não é um palíndromo: {frase_mod[::-1]}\n')