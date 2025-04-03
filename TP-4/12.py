"""
12. Pedí tres números al usuario y mostrá:
    El número mayor
    El número menor
    El valor absoluto del primer número
Funciones a practicar: max(), min(), abs()
"""

num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese otro numero: "))
num_3 = int(input("Ingrese un ultimo numero: "))

numMax = max(num_1, num_2, num_3)
numMin = min(num_1, num_2, num_3)
numAbsoluto = abs(num_1)

print(f"El numero maximo es: {numMax}, el numero minimo es: {numMin} y el valor absoluto del primer numero es: {numAbsoluto}")