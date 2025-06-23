# Lista de listas e seus índices

salas = [
    ['Maria', 'Helena', ],
    ['Elaine', ],
    ['Luis', 'João', 'Eduarda'],
]

print(salas)
print(salas[0][1])
print(salas[2][2])
print()


alunos_sala = ""

for indice, sala in enumerate(salas):
    print(f"# A sala {indice+1}:")
    
    for aluno in sala:
        alunos_sala += aluno
        print(aluno)
    
    print()
