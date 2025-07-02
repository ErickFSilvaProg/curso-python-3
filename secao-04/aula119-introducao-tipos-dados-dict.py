"""
- Dicionários em Python (Tipo Dict)

Dicionários são estruturas de dados do tipo par de 'chave' e 'valor':
    
    - Chave - podem ser consideradas como os 'índices' que vimos na lista e podem ser de tipos imutáveis como: str, int, float, bool, tuple, etc.

    - Valor - pode ser de qualquer tipo, incluindo outro dicionário.

Usamos as chaves '{}' ou a classe 'dict' para criar dicionários.

Imutáveis: str, int, float, bool, tuple.
Mutável: dict, list.
"""


# Exemplo 1:
pessoa_1 = dict(nome='Luiz Otávio', sobrenome='Miranda')
print(pessoa_1)
print()


#  Exemplo 2:
pessoa_2 = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'enderecos': [
        {
            'rua': 'tal tal',
            'numero': 123
        },
        {
            'rua': 'outra rua',
            'numero': 321
        }
    ]
}
print(pessoa_2, type(pessoa_2))
print()


# 
for chave in pessoa_2:
    print(chave, pessoa_2[chave])

print()