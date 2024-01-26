# Función para intercambiar valores si el primer argumento es menor que el segundo.
def Intercambiar(mayor, menor):
    if mayor < menor:
        return menor, mayor
    else:
        return mayor, menor

# Función para calcular el Máximo Común Divisor (MCD) utilizando el algoritmo de Euclides.
def CalcularMCD(num1, num2):
    # Se intercambian los valores si es necesario.
    num1, num2 = Intercambiar(num1, num2)
    
    # Se calcula el resto de la división.
    resto = num1 % num2
    
    # Si el resto es cero, se ha encontrado el MCD.
    if resto == 0:
        return num2
    else:
        # Si no es cero, se realiza una llamada recursiva con los nuevos valores.
        return CalcularMCD(num2, resto)

# Solicitar al usuario dos números enteros.
numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))

# Calcular e imprimir el MCD de los dos números ingresados.
print("MCD:", CalcularMCD(numero1, numero2))
