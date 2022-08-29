# Curso Python #15 - Interrompendo repetições while
# https://www.youtube.com/watch?v=1OFp_-R2B2A

# Apresentação do comando 'break' e o aproveitamento de loops infinitos

print("\nAULA #15 - Interrompendo repetições while")
print("--" * 16)

c = 0;
while True:
    print(f"{c}", end=" - ")
    if c == 10:
        break
    c += 1
print("Fim do while. O loop foi executado {c} vezes\n")

while True:
    print('Este while será executado enquanto o sinalizador não for N')
    sinalizador = input("Você gostaria de continuar? (S/N) ").upper()
    if sinalizador == "N":
        break
print("Fim do while\n")    