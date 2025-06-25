"""
Argumentos nomeados e não nomeados em funções Python.
'Argumento nomeado' tem nome com sinal de 'igual'.
'Argumento não nomeado' recebe apenas o argumento (valor).
"""

# Função soma com "argumentos não nomeados (posicionais)" e "argumentos nomeados":
def soma(x, y, z):

    # Definição.
    # Parâmetro é igual ao seu valor: {x=} ou y={y}.
    print(f"{x=} + y={y} + {z=}", "|", "x+y+z =", x + y + z)

# Chamar/executar a função:

# Passando argumentos não nomeados (posicionais):
print("- Argumentos não nomeados (posicionais):")
soma(1, 2, 3)
soma(2, 3, 1)
print()

# Passando argumentos nomeados:
# Obs.: Após o primeiro argumento ser nomeado, todos os outros deverão ser nomeados também.
print("- Argumentos nomeados:")
soma(x=1, y=2, z=3)
soma(y=2, z=3, x=1)
print()