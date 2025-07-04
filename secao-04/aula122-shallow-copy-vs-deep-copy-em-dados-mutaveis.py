"""
- Métodos úteis dos dicionários em Python.

len ou __len__ - informa quantas chaves tem no dicionário.
items - iterável que retorna as chaves e os valores no dicionário.
keys - iterável que retorna as chaves do dicionário.
values - iterável que retorna os valores do dicionário.
setdefault - adiciona valor se a chave não existe.
copy - retorna uma cópia rasa (shallow copy).
get - obtém uma chave.
pop - apaga um item com a chave específicada (del).
popitem - apaga o último item adicionado.
update - atualiza um dicionário com outro.

- Obs.: 
    Em Python, tudo é um objeto.
    Um dicionário não deixa de ser um objeto.
    Objetos tem métodos.
    Métodos estão dentro dos objetos.
"""

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

# Dessa forma não há cópia, mas sim um apontamento na memória.
d2 = d1

d2['c1'] = 10
print(d1)
print()


# Realizando uma 'cópia rasa'. Copia apenas os valores 'imutáveis'. Os valores 'mutáveis' são apontados no mesmo endereço da memória:
d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 9999

print(d1)
print(d2)
print()


# Para realisar um cópia profunda, proceda como no exemplo a seguir:

# Importe o 'módulo' 'copy' no início do código:
import copy

pessoa1 = {
    'Nome': 'João',
    'Idade': 35,
    'Profissão': 'Programador',
    'Números': [1, 2, 3]
}

# Cópia profunda:
pessoa2 = copy.deepcopy(pessoa1)

pessoa2['Nome'] = 'Erick'
pessoa2['Idade'] = 38
pessoa2['Números'] = [6, 856, 45]

print(pessoa1)
print(pessoa2)