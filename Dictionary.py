# Solicita al usuario que ingrese un número y lo convierte a entero
numero = int(input("Dime un número:"))

# Crea un diccionario llamado 'cuadrados'
cuadrados = {}

# Itera a través de los números desde 1 hasta el número ingresado por el usuario (inclusive)
for num in range(1, numero + 1):
    # Calcula el cuadrado de cada número y lo almacena en el diccionario 'cuadrados'
    cuadrados[num] = num ** 2

# Itera a través de los elementos del diccionario 'cuadrados'
for num, valor in cuadrados.items():
    # Imprime el número y su cuadrado en el formato especificado
    print("%d -> %d" % (num, valor))
