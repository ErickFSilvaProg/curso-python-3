# Formatação básica de strings:
# s - string
# d - int
# f - float
# .[número de dígitos]f
# x [ou] X - Hexadecimal
# [Caractere][><^][quantidade]
#   > - Esquerda
#   < - Direita
#   ^ - Centro
#   = - Força o número a aparecer antes dos zeros
# Sinal - + [ou] -
# Ex.: 0>-100,.1f
# Conversion flags - !r [__repr__] !s [__str__] !a


variavel1 = 'ABC'
variavel2 = 1000.4873648123746
variavel3 = -1000.4873648123746
variavel4 = 1500

print(f'{variavel1}.')
print(f'{variavel1: >9}.')
print(f'{variavel1: <9}.')
print(f'{variavel1: ^9}.')
print(f'{variavel1:*^9}.')
print('\n')

print(f'{variavel2:.1f}')
print(f'{variavel2:.2f}')
print(f'{variavel2:,.3f}') # Usa o separador decimal vírgula [,]
print(f'{variavel2:+,.4f}') # Exibe o valor com o [+] se for positivo
print(f'{variavel3:-,.5f}') # Exibe o valor com o [-] se for negativo
print(f'{variavel2:0=10,.3f}')
print('\n')

print(f'{variavel4:x}')
print(f'{variavel4:08x}')
print(f'{variavel4:X}')
print(f'{variavel4:08X}')
print('\n')

print(f'{variavel1}')
print(f'{variavel1!r}')
print(f'{variavel1!s}')
print(f'{variavel1!a}')