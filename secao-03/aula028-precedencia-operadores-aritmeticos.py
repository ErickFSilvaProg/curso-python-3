"""
- Precedência dos operadores:

1. (n + n) : "Precedência mais alta"
2. **      : Potenciação
3. *       : Multiplicação
   /       : Divisão
   //      : Divisão inteira
   %       : Módulo (resto da divisão)
4. +       : Adição
   -       : Subtração
"""

conta_1 = 1 + 1 ** 5 + 5
print(conta_1)

conta_2 = (1 + 1) ** (5 + 5)
print(conta_2)

conta_3 = (1 + (0.5 + 0.5)) ** (5 + 5)
print(conta_3)

conta_4 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_4)

conta_5 = 10 // 4
print(conta_5)