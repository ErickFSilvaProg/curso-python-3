"""
- Métodos úteis dos dicionários em Python.

len ou __len__ - informa quantas chaves tem no dicionário.
items - iterável que retorna as chaves e os valores no dicionário.
keys - iterável que retorna as chaves do dicionário.
values - iterável que retorna os valores do dicionário.
setdefault - adiciona valor se a chave não existe.
copy - retorna uma cópia rasa (shallow copy).
get - obtém o valor de uma chave do dicionário.
pop - apaga um item com uma chave específica do dicionário.
popitem - apaga o último item adicionado no dicionário.
update - atualiza um dicionário com outro dicionário.

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
print()

print(pessoa.items())
print()

print(pessoa.keys())
print()

print(pessoa.values())
print()

print(pessoa.setdefault('profissao', 'Programador'))
print()

print(pessoa.get('nome'), pessoa.get('sobrenome'))
print()

print(pessoa.pop('sobrenome')) # Apaga o dado da chave especificada no dicionário.
print(pessoa)
print()

print(pessoa.popitem()) # Apaga a última chave do dicionário.
print(pessoa)
print()

# 1ª forma do update:
pessoa.update({
    'nome': 'Erick Ferreira', # Tanto atualiza.
    'profissao': 'programador' # Como insere novos valores.
})
print(pessoa)
print()

# 2ª forma com o update: com tuplas
tupla = (('salario', '6.856,45'),) # Não precisa da vírgula no final se tiver mais de um item.
pessoa.update(tupla)
print(pessoa)
print()

# 3ª forma com o update: com listas
lista = [['linguagem', 'Python'],['Banco', 'PostgreSQL']]
pessoa.update(lista)
print(pessoa)
print()