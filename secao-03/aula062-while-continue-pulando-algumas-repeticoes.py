# While com o continue


contador = 0

while contador < 22:
    contador += 1

    if contador == 13:
        print("Não vou mostrar o 13")
        continue # O número '13' será pulado.

    print(contador)

    if contador == 20:
        break

print("\nAcabou...")