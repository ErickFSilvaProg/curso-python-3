# Desempacotamento em chamadas de métodos e funções.

string = "ABCD"
lista = ["Maria", "Helena", 1, 2, 3, "Eduarda"]
tupla = "Python", "é", "legal"
salas = [
    ['Maria', 'Helena', ],
    ['Elaine', ],
    ['Luis', 'João', 'Eduarda'],
]


# Desempacotamento normal:
a, b, *_, e, f = lista
print(a, f, e)
print()


# Desempacotamento em chamada de função:
for nome in lista:
    print(nome, end=", ")
print("\n")

print(*lista)
print(*string)
print(*tupla)
print("\n")

print(*salas, sep="\n")
