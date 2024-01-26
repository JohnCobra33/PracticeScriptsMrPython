# Función para verificar si un año es bisiesto
def es_bisiesto(year):
    # Un año es bisiesto si es divisible por 4 y no es divisible por 100, o es divisible por 400.
    if (year % 4 == 0 and not (year % 100 == 0)) or (year % 400 == 0):
        return True
    else:
        return False

# Función para obtener la cantidad de días en un mes dado un año
def dias_del_mes(month, year):
    # Meses con 31 días
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    # Meses con 30 días
    elif month in [4, 6, 9, 11]:
        return 30
    # Febrero, que puede tener 28 o 29 días dependiendo de si el año es bisiesto o no
    elif month == 2:
        if es_bisiesto(year):
            return 29
        else:
            return 28

# Función para calcular el día juliano dado un día, mes y año
def calcular_dia_juliano(day, month, year):
    diaj = 0
    # Suma los días de los meses anteriores al mes dado
    for mes in range(1, month):
        diaj += dias_del_mes(mes, year)
    # Agrega los días del mes actual
    diaj += day
    return diaj

# Función para leer una fecha desde la entrada del usuario
def leer_fecha():
    day = int(input("Día: "))
    month = int(input("Mes: "))
    year = int(input("Año: "))
    return day, month, year

# Función principal para calcular e imprimir el día juliano de una fecha
def dia_juliano():
    d, m, a = leer_fecha()
    print("Día Juliano:", calcular_dia_juliano(d, m, a))

# Programa principal
dia_juliano()
