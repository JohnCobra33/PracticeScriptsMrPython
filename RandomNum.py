"The application generates a random number from 1 to 100. Then, it prompts for guesses and responds whether the number to guess is greater or smaller than the input, along with the remaining attempts (you have 10 attempts to guess it). The program ends when the correct number is guessed (also telling you how many attempts it took), or if the maximum number of attempts is reached, it reveals the generated number."
import random

aleatorio = random.randint(1, 100)
print(aleatorio)

intentos = 0
max_intentos = 10

while (aleatorio != numusu) and (intentos < max_intentos):
    numusu = int(input("Ingresa un número del 1 al 100 "))
    intentos += 1

    if (numusu > aleatorio):
        print("El numero aleatorio es menor")
    elif (numusu < aleatorio):
        print("El numero aleatorio es mayor")
    else:
        print("")

    intentos_restantes = max_intentos - intentos
    if intentos_restantes > 0:
        print("Te quedan", intentos_restantes, "intentos.")

if (aleatorio == numusu):
    print("¡Ganaste! Has acertado el número aleatorio en", intentos, "intentos.")
else:
    print("Te has quedado sin intentos. El número correcto era:", aleatorio)
