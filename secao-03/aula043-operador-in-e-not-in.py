"""
- Operadores "in" (está em) e "not in" (não está em)

    Strings em python são iteráveis. É possível navegar item por item.

# Índices:

     0 1 2 3 4 5 (sequência positiva)
     O t á v i o
    -6-5-4-3-2-1 (sequência negativa)

"""

nome = "Otávio"

print(nome)
print(nome[2]) # Índice positivo
print(nome[-4]) # Índice negativo

print(10 * "*", "\n")

print("á" in nome)
print("z" in nome)

print(10 * "*", "\n")

print("vio" not in nome)
print("zero" in nome)

print("*" * 10, "\n")


# Exemplo:
nome = input("Digite um texto: ")
print(nome)
print()

while True:

    encontrar = input("O que deseja encontrar?: ")
    print()

    if encontrar == "sair" or encontrar == "Sair" or encontrar == "SAIR":
        break

    if encontrar in nome:
        print(f"Busca encontrada")
        print(f"[{encontrar.upper()}] existe em: {nome}")
    else:
        print(f"Busca não encontrada")

    print()
print()