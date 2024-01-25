notas = []

for indice in range(1, 6):
    nota_valida = False

    while not nota_valida:
        nota = int(input("Introduce la nota %d:" % indice))

        if nota < 0 or nota > 10:
            print("La opción que has elegido no es válida (tiene que ser entre 0 y 10)")
        else:
            nota_valida = True
    

    notas.append(nota)

print("Notas: ", end="")
for nota in notas:
    print(nota, " ", end="")

print("\nNota Media: ", sum(notas) / len(notas))
print("Nota máxima: ", max(notas))
print("Nota mínima: ", min(notas))
