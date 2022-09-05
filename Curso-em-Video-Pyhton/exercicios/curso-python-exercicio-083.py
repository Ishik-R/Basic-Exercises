# Exercício Python #083 - Validando expressões matemáticas
# https://www.youtube.com/watch?v=dvhP41Z7TLk

# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#  Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

print("\n#083 - Validando expressões matemáticas")
print("--" * 16)
expressao = input("Digite sua expressão matemática: ").strip()
v = 0
for caracter in expressao:
    if caracter == '(':
        v += 1
    if caracter == ')':
        v -= 1
    if v < 0:
        break
if v == 0:
    print("Sua expressão é válida!")
else:
    print("Sua expressão não é válida. Há algo errado com os parênteses.")    