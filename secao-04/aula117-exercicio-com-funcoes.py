"""
- Exercícios:

1. Crie funções que duplicam, triplicam e quadruplicar o número recebido como parâmetro.
"""

# Exemplo 1:
def criar_multiplicador_1(multiplicador):
    
    def multiplicar(numero):
        return numero * multiplicador
    
    return multiplicar


duplicar = criar_multiplicador_1(2)
triplicar = criar_multiplicador_1(3)
quadruplicar = criar_multiplicador_1(4)

print(duplicar(10))
print(triplicar(10))
print(quadruplicar(10))

print()


# Exemplo 2:
def criar_multiplicador_2(valor_1, valor_2):
    
    def duplicador(valor_1):
        return valor_1 * 2

    def triplicador(valor_2):
        return valor_2 * 3
    
    lista_valores = [duplicador(valor_1), triplicador(valor_2)]
    return lista_valores


for numero in criar_multiplicador_2(100, 100):
    print(numero)
