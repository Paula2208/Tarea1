'''
Ejercicio 0:
    Escribir un programa que calcule la suma de los 
    primeros N números naturales pares, donde N es 
    proporcionado por el usuario.
'''

N = int(input("\nHola (•◡•)/\n Ingresa el valor de N: "))

# ¡Ojo! El primer número par natural es el 0

sum = 0
for i in range(0, N):
    sum += 2*i

print(f"\nLa suma de los primeros {N} números naturales pares es: {sum}\n")