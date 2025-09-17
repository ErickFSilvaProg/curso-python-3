"""
- Introdução ao 'for/in' - Estrutura de reperição para repetições finitas.

"""

# Exemplo de laço com interação finita:
texto = "Python"
novo_texto = ""
i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(f"{texto[i]}:{i}")
    i += 1

print("\n-----------------\n")

"""
# Exemplo de laço com interação infinita:
senha_salva = "123456"
senha_digitada = ""
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f"Sua senha ({repeticoes}x): ")
    repeticoes += 1

print("\nAquele laço acima pode ter repetições infinitas.")

print("\n-----------------\n")

"""

# Exemplo de laço com interação finita:
for letra in texto:
    novo_texto += f"*{letra}"
    print(letra)

print(f"\n{novo_texto}*\n")