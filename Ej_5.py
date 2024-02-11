'''
Ejercicio 5:
    Escribir una función que tome una
    lista y un elemento como argumentos y
    devuelva True si el elemento está presente
    en la lista y False en caso contrario.
'''

def checkElement(arr, elem):
    return elem in arr

# Ejemplo
print("\nHola (•◡•)/")

arr1 = [7, 12, 3, 7, 5]
elem1 = 1
elem2 = 5

isIn1 = checkElement(arr1, elem1)
isIn2 = checkElement(arr1, elem2)

print(f"¿El elemento {elem1} está presente en la lista? {isIn1}")
print(f"¿El elemento {elem2} está presente en la lista? {isIn2}")
print()