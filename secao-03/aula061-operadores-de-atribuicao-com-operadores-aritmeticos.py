"""
- Operadores de atribuição com operadores aritméticos:

    =     -> Atribuição simples.
    **=   -> Potenciação e atribuição.
    *=    -> Multiplicação e atribuição.
    /=    -> Divisão e atribuição.
    //=   -> Divisão inteira e atribuição.
    %=    -> Módulo e atribuição.
    +=    -> Adição e atribuição.
    -=    -> Subtração e atribuição.

"""

# Atribuição simples:
contador = 10
print(contador)

# Potenciação e atribuição:
contador **= 2
print(contador)

# Multiplicação e atribuição:
contador *= 2
print(contador)

# Divisão e atribuição:
contador /= 2
print(contador)

# Divisão inteira e atribuição:
contador //= 2
print(contador)

# Módulo e atribuição:
contador %= 2
print(contador)

# Adição e atribuição:
contador += 2
print(contador)

# Subtração e atribuição:
contador -= 2
print(contador)
print()


# Exemplo com o while:
numero = 2

while numero <= 1024:
    print(numero)
    numero *= 2
print()