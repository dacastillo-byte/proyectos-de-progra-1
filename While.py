import random

def jugar():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    limite_intentos = 7

    while intentos < limite_intentos:
        intento = int(input("Adivina el numero entre 1 y 100: "))
        intentos += 1
        
        if intento < numero_secreto:
            print("mas alto")
        elif intento > numero_secreto:
            print("mas bajo")
        else:
            print(F"felicidades 🎉🍾🥳adivinaste el numero en {intentos} intentos")
            return

    if intentos == limite_intentos:
        print("superaste el numero de intentos permitido")
        print(F"el numero secreto era: {numero_secreto}")

# Bucle principal del juego
while True:
    jugar()
    reiniciar = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
    if reiniciar != 's':
        print("¡Gracias por jugar!")
        break