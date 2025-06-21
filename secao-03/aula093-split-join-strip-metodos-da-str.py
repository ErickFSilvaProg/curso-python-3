"""
split e join com list e str:

split - divide uma string
join - une uma string
strip - corta os espaços nos dois lados
rstrip - corta os espaços na direita
lstrip - corta os espaços na esquerda
"""

frase = "  Olha só, que coisa interessante.   "
lista_frases_cruas = frase.split(",")
lista_frases = []
frases_unidas = ...


# split - Dividindo string:
lista_frases_1 = frase.split()
lista_frases_2 = frase.split(",") # Separa pela 'vírgula'.
lista_frases_3 = frase.split(", ") # Separa pela 'vírgula' e pelo 'espaço' após a virgula.

print(lista_frases_1)
print(lista_frases_2)
print(lista_frases_3)
print()


for i, frase in enumerate(lista_frases_2):
    print(lista_frases_2[i])
print()

for i, frase in enumerate(lista_frases_2):
    print(lista_frases_2[i].strip())
print()

for i, frase in enumerate(lista_frases_2):
    print(lista_frases_2[i].rstrip())
print()

for i, frase in enumerate(lista_frases_2):
    print(lista_frases_2[i].lstrip())
print()

# Maneira não recomendada:
print("Antes do strip:", lista_frases_2)
for i, frase in enumerate(lista_frases_2):
    lista_frases_2[i] = lista_frases_2[i].strip()

print("Após o strip:", lista_frases_2)
print()

# Maneira recomendada:
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)


# join - Unindo string:
frases_unidas = "-".join("abc")
print(frases_unidas)

frases_unidas = ", ".join(lista_frases)
print(frases_unidas)