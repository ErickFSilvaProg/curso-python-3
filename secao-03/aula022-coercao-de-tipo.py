"""
Conversão de tipos, coersão.
Type convertion, typecasting ou coercion é o ato de converter um tipo em outros tipos imutáveis e primitivos.

Tipos Imutáveis e Primitivos: str, int, float, bool.
"""

# int:
print('1', type('1'))
print(int('1'), type(int('1')))
print(int('1') + 1)

# float:
print(float('1') + 1)
print(type(float('1') + 1))

# bool:
print(bool(''))
print(bool(' '))

# float:
print(str(11) + 'b')