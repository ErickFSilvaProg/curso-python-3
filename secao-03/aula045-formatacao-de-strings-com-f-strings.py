"""
# Formatação básica de strings:

    s - string
    d - int
    f - float
    .[número de dígitos]f
    x ou X - Hexadecimal
    
    [Caractere][><^][quantidade]
        
        > - esquerda
        < - direita
        ^ - centro
        = - força o sinal a aparecer antes dos zeros
    
    Sinal : + ou -

        Ex.: 0>-100,.1f
    
    Conversion flags: !r [__repr__] !s [__str__] !a [__ask__]

"""

variavel1 = "ABC"
variavel2 = 1000.4873648123746
variavel3 = -1000.4873648123746
variavel_hexa = 1500

print(f"|{variavel1}|")
print(f"|{variavel1: >9}|")
print(f"|{variavel1: <9}|")
print(f"|{variavel1: ^9}|")
print(f"|{variavel1:*^9}|")
print()

print(f"{variavel2}")
print(f"{variavel2:.1f}") # Formata com uma casa decimal.
print(f"{variavel2:.2f}") # Formata com duas casas decimais.
print(f"{variavel2:,.3f}") # Formata com três casas decimais e com o separador decimal vírgula [,].
print(f"{variavel2:+,.4f}") # Formata com quatro casas decimais e com o separador decimal vírgula. Se o número for positivo exibe o [+].
print(f"{variavel3:-,.5f}") # Formata com cinco casas decimais e com o separador decimal vírgula. Se o número for negativo exibe o [-].
print()

print(f"{variavel2:0>+10,.1f}")
print(f"{variavel2:0=+10,.1f}") # O [=] força o sinal a aparecer antes dos zeros.
print()

print(f"{variavel_hexa}")
print(f"O hexadecimal de {variavel_hexa} é {variavel_hexa:x}")
print(f"{variavel_hexa:08x}")
print(f"{variavel_hexa:X}") # Coloca as letras em caixa alta.
print(f"{variavel_hexa:08X}") # Coloca as letras em caixa alta.
print()

print(f"{variavel1}")
print(f"{variavel1!r}")
print(f"{variavel1!s}")
print(f"{variavel1!a}")
print()