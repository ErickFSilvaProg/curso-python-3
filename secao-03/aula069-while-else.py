# While/else

nome = "Erick|Ferreira"
i = 0

while i < len(nome):
    letra = nome[i]

    if letra == " ":
        break

    print(letra)
    i += 1

else:
    print("Não encontrei um espaço na 'string'")

print("Fora do 'While.'")