"""
Conversões de tipos, coersão.
'Type convertion', 'typecasting' ou 'coercion' é o ato de converter um tipo em outros tipos imutáveis e primitivos.

Tipos imutáveis e primitivos: str, int, float e bool.

Python é uma liguagem de programação dinâmica e forte!
"""

print("a" + "b")
# print('1' + 1) Retorna um erro.
print()

# Coerção para int:
print(type(1), 1)
print(type(int("1")), int("1"))
print(int("1") + 1)
print()

# Coerção para float:
print(type(float("1")), float("1"))
print(float("1") + 1)
print()

# Coerção para bool:
print(bool('')) # A coerção com uma string vazia retorna um 'False'.
print(bool(" ")) # A coerção de uma string não vazia retorna um 'True'.
print()

# Coerção para float:
print(str(11) + "b")