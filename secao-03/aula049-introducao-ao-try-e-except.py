"""
- Introdução ao try/except:

try - tentar executar o código.
except - ocorreu algum erro ao tentar executar o código.

Obs.: O "input()" sempre retornará uma string.
      Tudo em Python é um objeto.

isdigit: verifica se o usuário digitou apenas "números".
"""

print(123)
print(456)
# int("a") - ValueError: invalid literal for int() with base 10: 'a'
print()


numero_str = input("Vou dobrar o número que você digitar: ")
print()

# O "if" não evita erros (exceções), apenas executa o código.
# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f"O dobro de {numero_str} é {numero_float * 2}.")
# else:
#     print("Isso não é um número.")
# print()

# O "try/except" trata o erro.
try:
    print(type(numero_str), numero_str)
    numero_float = float(numero_str)
    print(type(numero_float), numero_float)
    print(f"\nO dobro de {numero_str} é {numero_float * 2}.")
except:
    print("Isso não é um número.")
print()