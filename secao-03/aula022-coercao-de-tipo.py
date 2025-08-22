"""
Conversão de tipos: coerção.

'Type convertion', 'typecasting' ou 'coercion' é o ato de converter um tipo em outros tipos imutáveis e primitivos.

Tipos imutáveis e primitivos: str, int, float e bool.

Python é uma linguagem de programação dinâmica e forte!

"""

# Primitivos e imutáveis:
print("- Primitivos e imutáveis:")
print("a" + "b")
# print("1" + 1) Retorna o erro: TypeError.
print("1" + "1")
print(1 + 1)
print()

# Coerção str para int:
print("- Coerção para int:")
print(type("1"), "1")
print(type(int("1")), int("1"))
print(type(int("1") + 1), int("1") + 1)
print()

# Coerção str para float:
print("- Coerção para float:")
print(type("1.1"), "1.1")
print(type(float("1.1")), float("1.1"))
print(type(float("1.1") + 1), float("1.1") + 1)
print()

# Coerção str para bool:
print("- Coerção str para bool:")
# A coerção com uma string vazia retorna um 'False'.
print(bool(""))
# A coerção com uma string não vazia retorna 'True'.
print(bool(" "))
print(bool("a"))
print(bool("1"))
print()

# Coerção int para str:
print("- Coerção int para str:")
print(type(11), 11)
print(type(str(11)), str(11))
print()

# Coerção float para str:
print("- Coerção float para str:")
print(type(1.1), 1.1)
print(type(str(1.1)), str(1.1))
print()