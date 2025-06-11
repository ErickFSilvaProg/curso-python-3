# Iterando strings co while.

cont1 = 0
cont2 = 0
nome = "Erick"
novo_nome = ""
tamanho_nome = len(nome)

while cont1 < tamanho_nome:
    print(nome[cont1])
    cont1 += 1


print()
while cont2 < tamanho_nome:
    letra = nome[cont2]
    novo_nome += f"*{letra}"
    cont2 += 1

print(novo_nome)