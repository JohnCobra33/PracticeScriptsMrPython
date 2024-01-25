#Declaramos las variables
Distancia = int(input("Introduce la distancia en Km: "))
Moto1 = int(input("Introduce la velocidad de la moto 1 en Km/h: "))
Moto2 = int(input("Introduce la velocidad de la moto 2 en Km/h: "))

velomoto = Moto2 - Moto1

# Calcula el tiempo en horas y minutos
tiempo_en_horas = Distancia / velomoto
tiempo_en_minutos = tiempo_en_horas * 60

# Divide el tiempo total en horas y minutos
horas = int(tiempo_en_horas)
minutos = int((tiempo_en_minutos - horas * 60))

print("Las motos se encontrarán en: {} horas y {} minutos".format(horas, minutos))
