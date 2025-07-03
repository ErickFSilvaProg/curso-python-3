"""
- Manipulando chaves e valores em dicionários
"""

# Criando um dicionário vazio:
pessoa = {}
print(pessoa)

# Adicionando chave ao dicionário:
pessoa['nome'] = 'Erick'
print(pessoa)

pessoa["profissao"] = "Programador"
print(pessoa)

# Adicionando chave dinâmica ao dicionário:
chave_dinamica = "sobrenome"
pessoa[chave_dinamica] = "Ferreira"
print(pessoa)

# Apagando uma chave:
del pessoa["sobrenome"]
print(pessoa)

# 
pessoa["sobrenome"] = "Ferreira"
print(pessoa)

# Obs.: O 'if' não trata erros no código. Para não parar o código, utilize após o 'if': 'dicionario.get("valor", None)'
if pessoa.get("profissao"):
    print(f"Profissão: {pessoa["profissao"]}")
else:
    print(pessoa)