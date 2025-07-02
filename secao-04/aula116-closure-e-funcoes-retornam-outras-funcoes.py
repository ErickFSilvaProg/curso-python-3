"""
Closure e funções que retornam outras funções.

Função em Python que não retorna nada, retorna 'None'.
"""

def criar_saudacao(saudacao):
    
    def saudar_pessoa(nome):
        return f"{saudacao}, {nome}!"

    return saudar_pessoa

falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_noite = criar_saudacao("Boa noite")

# print(falar_bom_dia("Luiz"))
# print(falar_boa_noite("Luiz"))

for nome in ["Maria", "Joana", "Luiz"]:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))