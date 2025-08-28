"""
    - Interpolação básica de strings:

        s - string
        d ou i - int
        f - float
        x ou X - hexadecimal (0123456789ABCDEF)
"""

nome = "Luiz"
preco = 1000.95897643
int_hexa = 15

variavel = "%s, o preço total foi %.2f" % (nome, preco)

print(variavel)
print("O hexadecimal de %d é %x" % (int_hexa, int_hexa))