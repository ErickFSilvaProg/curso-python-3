"""
- Tipos primitivos: int e float.

    int -> Números inteiros.

        O tipo primitivo 'int' representa qualquer número positivo ou negativo. 'int' sem o sinal negativo (-) é considerado positivo.
    
    float -> Número com ponto flutuante.

        O tipo primitivo 'float' representa qualquer número positivo ou negativo com ponto flutuante. 'float' sem o sinal negativo (-) é considerado positivo.
    
A classe 'type()' mostra o tipo que o python inferiu ao valor.

No programação sempre utilizaremos um ponto (.) para separar as casas decimais de um número.

Obs.: Tudo em python é um objeto.

"""

# int:
print("- int:")
print(11) # int positivo.
print(-11) # int negativo.
print(0) # int.
print()

#  float:
print("- float:")
print(1.1) # float positivo.
print(-1.3) # float negativo.
print(0.0) # float.
print()

# type(): Função para ver o tipo do valor.
print("- type():")
print(type("Python"), "Python")
print(type(10), 10, type(-10), -10)
print(type(1.10), 1.10, type(-1.10), -1.10)
print()