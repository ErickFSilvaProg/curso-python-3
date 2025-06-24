"""
Introdução às funções (def) em Python.
Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções Python retornam 'None' (não valor).
"""

# Definindo funções personalizadas em Python:
def imprimir(a, b, c): # Os parâmetros são definidos aqui.
    print(a, b, c)

imprimir("'def' - Função", "personalizada", "em Python") # Os argumentos são passados aqui.
imprimir(1, 2, 3)
print()


def saudacao(nome="Sem nome"): # Parâmetro com um argumento padrão.
    print(f"Olá, {nome}!")

saudacao("Erick")
saudacao("Manoel")
saudacao()
print()

