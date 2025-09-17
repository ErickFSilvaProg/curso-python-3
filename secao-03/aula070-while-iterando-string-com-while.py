"""
# While - Iterando string com while.

    - Quando precisar quebrar uma liha em Python utilize: (barra invertida)

"""

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ""
frase = "O Python é uma linguagem de programação" \
        "multiparadigma." \
        "Python foi criado por Guido Van Rossum.".lower()

# Qual a letra que apareceu mais vezes nessa frase?:
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == " ":
        i += 1
        continue

    qtd_atual_letra = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_atual_letra:
        qtd_apareceu_mais_vezes = qtd_atual_letra
        letra_apareceu_mais_vezes = letra_atual
    
    i += 1

print(f"A letra que apereceu mais vezes foi: {letra_apareceu_mais_vezes}. \nAperecendo {qtd_apareceu_mais_vezes}x.")
print()