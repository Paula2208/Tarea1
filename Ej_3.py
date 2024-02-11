'''
Ejercicio 3:
    Escribir una función que tome una
    lista de números como argumento y
    devuelva el promedio de esos números.
'''

def getAverage(lista):
    if len(lista) == 0:
        return 0  # Si la lista está vacía, el promedio es cero para evitar divisiones por cero
    
    sum_total = sum(lista)
    return sum_total / len(lista)

# Ejemplo
print("\nHola (•◡•)/")

nums = [4, 1, 3, 7, 12]
average = getAverage(nums)

print("El promedio de los elementos de la lista es:", average)
print()