# Estrutura de repetição - While e break

while True:
    nome = input("Qual o seu nome: ")

    if nome != "sair":
        print(f"Seu nome é {nome}\n")

    else:
        break

print("\nAcabou...")