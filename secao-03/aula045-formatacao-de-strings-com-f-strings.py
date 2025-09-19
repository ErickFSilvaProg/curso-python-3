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

var1 = "Python"
var2 = 1000.4873648123746
var3 = -1000.4873648123746
var_hexa = 1500

print("[1234567890]")
print(f"|{var1}|")
print(f"|{var1: >10}|") # Acrescenta espaços do lado esquerdo da string totalizando dez caracteres.
print(f"|{var1: <10}|") # Acrescenta espaços do lado direito da string totalizando dez caracteres.
print(f"|{var1: ^10}|") # Acrescenta espaços nos dois lados da string, esquerdo e direito, totalizando dez caracteres.
print(f"|{var1:*^10}|") # Acrescenta asteríscos nos dois lados da string, esquerdo e direito, totalizando dez caracteres.
print()

print(f"{var2}")
print(f"{var2:.1f}") # Formata com uma casa decimal.
print(f"{var2:.2f}") # Formata com duas casas decimais.
print(f"{var2:,.3f}") # Formata com três casas decimais e com o separador de milhar vírgula [,].
print(f"{var2:+,.4f}") # Formata com quatro casas decimais e com o separador decimal vírgula. Se o número for positivo exibe o [+].
print(f"{var3:-,.5f}") # Formata com cinco casas decimais e com o separador decimal vírgula. Se o número for negativo exibe o [-].
print()

print(f"{var2:0>+10,.1f}")
print(f"{var2:0=+10,.1f}") # O [=] força o sinal a aparecer antes dos zeros.
print()

print(f"{var_hexa}")
print(f"O hexadecimal de {var_hexa} é {var_hexa:x}")
print(f"{var_hexa:08x}")
print(f"{var_hexa:X}") # Coloca as letras em caixa alta.
print(f"{var_hexa:08X}") # Coloca as letras em caixa alta.
print()

print(f"{var1}")
print(f"{var1!r}")
print(f"{var1!s}")
print(f"{var1!a}")
print()