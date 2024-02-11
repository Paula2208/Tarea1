'''
Ejercicio 2:
    Implementar una función que calcule
    el área de un círculo dado su radio.
'''

#Librería matemática
import math

def circle_area(rad):
    return math.pi *(rad**2)

# Ejemplo

print("\nHola (•◡•)/")

rad = float(input("Ingresa el radio del círculo: "))
area = circle_area(rad)

print("El área del círculo es:", area)
print()