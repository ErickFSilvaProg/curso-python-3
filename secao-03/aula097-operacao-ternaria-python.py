"""
Operação ternária (condicional de uma linha):
[valor] if [condição] else [Outro valor]
"""

# 
condicao_1 = 10 == 10
condicao_2 = 10 == 11
variavel_1 = "Valor" if condicao_1 else "Outro valor"
variavel_2 = "Valor" if condicao_2 else "Outro valor"

print(variavel_1)
print(variavel_2)
print()


# 
digito = 8
novo_digito = digito if digito <= 9 else 0
print(novo_digito)

novo_digito = 0 if digito > 9 else digito
print(novo_digito)
print()


# 
print("Valor" if False else "Outro valor" if False else "Fim")