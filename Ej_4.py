'''
Ejercicio 4:
    Realizar un programa que tome una
    lista de números como entrada y 
    devuelva una nueva lista que contenga
    solo los números pares de la lista original.
'''

numsString = input("\nHola (•◡•)/\nIngresa los números de la lista separados por espacios: ")

# Sacar los números de la lista del string de entrada
strings = numsString.split(" ")
nums = []
actual = 0

for i in strings:
    try:
        # Convertir a número
        actual = float(i)
        if(actual % 2 == 0):
            # Seleccionar sólo los números pares
            nums.append(actual)
    except:
        print(f"Error trying to convert {i} to number")

print("Números pares:", nums)
print()