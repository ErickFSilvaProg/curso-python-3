"""
    - Tipo String: Textos.

        str -> string -> texto
        Strings são textos que estão dentro de aspas.

    Python: Linguagem de programação.
    Tipagens - Dinâmica: O Python sabe qual é o tipo da variável apenas pelo valor inserido.
               Forte: O Python garante a segurança evitando coerção automática entre tipos incompatíveis.

               Exemplo: print(1 + '1') TypeError: unsupported operand type(s) for +: 'int' and 'str'
    
"""

# Exemplo de tipagem dinâmica:
print('- Exemplo de tipagem dinâmica:')
print(type(1234), 1234)
print(type('1234'), '1234')
print()

# Aspas simples:
print('- Aspas simples:')
print(type('Erick Ferreira'), 'Erick Ferreira')
print()

# Aspas duplas:
print('- Aspas duplas:')
print(type("Erick Ferreira"), "Erick Ferreira")
print()

# Caractere de 'escape': Barra invertida '\'.
print('Caractere de escape: Barra invertida -> \ ')
print(type("Dev Python e \"Programador Web\""), "Dev Python e \"Programador Web\"")
print()

# 'r': Utilizado em expressoes regulares. Também exibe o caractere de escape na tela.
print("- 'r' -> Utilizado em expressões regulares.")
print(type(r"Dev. Python e \"Programador Web\""), r"Dev. Python e \"Programador Web\"")
print()