"""
- Introdução ao try/except:

try - tentar executar o código.
except - ocorreu algum erro ao tentar executar o código.

isdigit: verifica se o usuário digitou "apenas números"
"""


numero_str = input('Dobrar o número: ')
print('\n')

# O "if" não trata o erro, apenas executa o código.
if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2}')

else:
    print('Isso não é um número.')


print('\n*\n')


# O "try/except" trata o erro.
try:
    print(type(numero_str), numero_str)
    numero_float = float(numero_str)
    print(type(numero_float), numero_float)
    
    print(f'O dobro de {numero_str} é {numero_float * 2}')

except:
    print('Isso não é um número.')