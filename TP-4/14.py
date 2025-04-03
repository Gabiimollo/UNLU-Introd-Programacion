"""
14. Genere un programa que solicite al usuario un número entero (de 0 a 255) e imprima en 
pantalla el número convertido a binario.
"""

# Solicitar al usuario un número entero entre 0 y 255
numero = int(input("Ingrese un número entero entre 0 y 255: "))

# Convertir el número a binario y mostrarlo en pantalla
binario = bin(numero)
print(f"El número {numero} en binario es: {binario}")