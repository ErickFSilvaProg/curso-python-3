"""
- Como o 'for' funciona por trás dos panos:

Iterável -> str, range, etc(__iter__).
Iterador -> quem sabe entregar um valor por vez.
iter -> me entregue seu iterador.
next -> me entregue o próximo valor.
"""

texto = "Luiz" # iterável
iterador = iter(texto) # iterator

# É assim que o 'for' funciona:
while True:
    
    try:
        letra = next(iterador)
        print(letra)
    
    except StopIteration:
        break

print()

# Na pática é apenas isso:
for letra in texto:
    print(letra)