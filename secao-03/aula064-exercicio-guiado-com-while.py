# Iterando strings com while.

#                 1         2
#       01234567890123456789012
nome = "Erick Ferreira da Silva"
tamanho_nome = len(nome)

print(nome)
print(tamanho_nome)
print()


indice = 0
novo_nome = ""

while indice < tamanho_nome:
    novo_nome += f"*{nome[indice]}"
    indice += 1

print(f"{novo_nome}*")
print()