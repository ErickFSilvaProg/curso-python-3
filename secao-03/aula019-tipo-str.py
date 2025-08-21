# Tipos String: Textos.

"""
Python: Linguagem de programação.
Tipagem: Dinâmica / Forte.
str -> string -> texto.
Strings são textos que estão dentro de aspas.

"""

# Tipagem dinâmica: O python sabe o tipo do dado inserido.
print(type(1234), 1234)
print(type("1234"), "1234")
print()

# Aspas simples:
print(type('Erick Ferreira'), 'Erick Ferreira')
print()

# Aspas duplas:
print(type("Programador 'Python'"), "Programador 'Python'")
print()

# Caractere de 'escape': Barra invertida '\'.
print(type("Dev. Python e \"Cientista de Dados\""), "Dev. Python e \"Cientista de Dados\"")
print()

# 'r': Utilizado em expressões regulares.
# Também exibe o caractere de escape na tela.
print(type(r"Dev. Python e \"Cientista de Dados\""), r"Dev. Python e \"Cientista de Dados\"")
print()