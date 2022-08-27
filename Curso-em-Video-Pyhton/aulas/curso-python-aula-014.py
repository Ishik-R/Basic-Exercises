# Curso Python #014 - Estrutura de repetição while
# https://www.youtube.com/watch?v=LH6OIn2lBaI

# Apresentação da estrutura de repetição 'while'

print("\nAULA #014 - Estrutura de repetição while")
print("--" * 16)

c = 0;
while c < 5:
    print('Essa mensagem será exibida 5 vezes')
    c += 1
print('Fim do while\n')

c = 10;
while c > 2:
    print(f'O número da vez é {c}')
    print('Podemos inserir vários comandos dentro do laço!')
    c = c - 2
print('Fim do while\n')

start = 1
finish = 5
step = 1
while start <= finish:
    print(f'Número atual: {c}. Vamos até {finish}')
    start = start + step
print('Fim do while\n')

sinalizador = 'S'
while sinalizador != 'N':
    print('Este while será executado enquanto o sinalizador não for N')
    sinalizador = input('Você gostaria de continuar? (S/N) ')
print('Fim do while\n')    