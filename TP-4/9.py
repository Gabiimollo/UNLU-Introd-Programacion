"""
9.  Cree un script que le solicite al usuario ingresar tres números y muestre 
por pantalla el número máximo y mínimo.
"""

num_1 = input("Ingrese el numero 1")
num_2 = input("Ingrese el numero 2")
num_3 = input("Ingrese el numero 3")

numeroMayor = max(num_1, num_2, num_3)
numeroMenor = min(num_1, num_2, num_3)

print(f"El número mayor es: {numeroMayor}")
print(f"El número menor es: {numeroMenor}")