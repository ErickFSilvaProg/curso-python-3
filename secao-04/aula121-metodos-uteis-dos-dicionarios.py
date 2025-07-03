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

pessoa = {
    'nome': 'Erick',
    'sobrenome': 'Ferreira',
    'idade': 38,
    'altura': 1.75
}


print(pessoa.__len__())
print(pessoa.items())
print(pessoa.keys())
print(pessoa.values())
print(pessoa.setdefault('profissao', 'Programador'))
print(pessoa)
print(pessoa)
print(pessoa)
print(pessoa)
print(pessoa)