"""
- Introdução ao desempacotamento

"""

nomes = ["Maria", "Helena", "Luiz"]
nome1, nome2, nome3 = nomes
nome4, nome5, nome6 = ["João", "Antônio", "Erick"]

# O '_' é uma convensão utilizada no Python.
_, nome7, *__ = ["Gustavo", "Pedro", "Miguel", "Alex", "Tereza", "Daniel"]

print(nome1)
print(nome2)
print(nome3)
print(nome4)
print(nome5)
print(nome6)
print(nome7)
print(_)

for nome in __:
    print(nome)