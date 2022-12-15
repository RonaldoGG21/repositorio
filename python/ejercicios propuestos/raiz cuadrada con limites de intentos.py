#sacar la raiz cuadrada de un numero no negativo, si lo introduces mas de 3 veses que no te deje introducir datos

# ESTO ES PYTHON

import math

print("Protocolo Animal")
numero = int(input("introduce el numero para su raiz cuadrada: "))
intentos = 0

while numero<0:
    print("No dijites un numero negativo")
    # sal del while si lo intenta mas de 3 veses
    if intentos==2:
        print("cagaste piola intentalo mas tarde")
        break

    numero = int(input("introduce el numero para su raiz cuadrada: "))
    # sumador de intentos
    if numero<0:
        intentos+=1

if intentos<2:
    # sqrt saca la raiz cuadrada para que este metodo funcione devemos de tener la clase math activada o importada
    solucion = math.sqrt(numero)
    print(solucion)
    print(" su cuadrado de " + str(numero) + " es " + str(solucion)) 