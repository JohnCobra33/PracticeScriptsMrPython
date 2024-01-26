notas = []
for indice in range(1,6):
  nota_pablo = False

  while not nota_pablo:
    nota = int(input("Introduce la nota %d:" % indice))
    if nota < 0 or nota > 10: 
      print("La opción que has elegido no es válida (tiene que ser entre 0 y 10)")
    else:
      nota_pablo = True
  notas.append(nota)

# Muestro resultados

print("Notas: ",end="")
for nota in notas:
	print(nota," ",end="")
print()
print("Nota media: ",sum(notas)/len(notas))
print("Nota max: ",max(notas))
print("Nota min: ",min(notas))
