'''
Ejercicio 1:
    Escribir un programa que combine 
    dos listas ordenadas en una lista 
    ordenada.
'''

print("\nHola (•◡•)/")

# Ejemplo
arr1 = [1, 2, 3, 5, 7, 8]
arr2 = [2, 4, 6, 8, 9, 10]

final_arr = []

# Apuntadores
i = 0
j = 0

# Se van comparando ambas listas en orden ascendente para
# seleccionar el menor del espacio donde está el apuntador

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        final_arr.append(arr1[i])
        i += 1
    else:
        final_arr.append(arr2[j])
        j += 1

# Se añade el resto de la lista al array final porque
# ya se han revisado todos los más pequeños
final_arr.extend(arr1[i:])
final_arr.extend(arr2[j:])

print("Lista combinada ordenada:", final_arr)
print()