"""
Higher Order Functions - Funções de Primeira Classe
Funções que podem receber e/ou retornar outras funções.
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, "Bom dia!", "Luiz")
)

print(
    executa(saudacao, "Boa noite", "Maria")
)