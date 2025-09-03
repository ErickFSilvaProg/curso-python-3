"""
- Estrutura de repetição: While e break.

    Executa uma ação enquanto uma condição for verdadeira.
    Loop infinito -> Quando o código não tem fim.
"""

condicao = True

while condicao:
    nome = input("Qual o seu nome: ")

    if nome != "sair":
        print(f"Seu nome é {nome}\n")
    else:
        break

print("Acabou...")
print()