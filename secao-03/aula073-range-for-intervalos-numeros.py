"""
# for + range

    - range -> range(start, stop, step):

        Quando é passado apenas um valor, esse valor é o stop.

"""


numeros = range(10) # O último valor não será impresso.
print(numeros)

for numero in numeros:
    print(numero)


print("\n---------------------")
numeros = range(1, 11) # O último valor não será impresso.
print(numeros)

for numero in numeros:
    print(numero)


print("\n---------------------")
numeros = range(1, 11, 2) # O último valor não será impresso.
print(numeros)

for numero in numeros:
    print(numero)


print("\n---------------------")
numeros = range(10, 0, -1) # O último valor não será impresso.
print(numeros)

for numero in numeros:
    print(numero)