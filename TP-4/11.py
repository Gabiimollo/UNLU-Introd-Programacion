"""
11. Pedí al usuario un número con decimales y mostrá (ayudate con round()):
    El número redondeado hacia el entero más cercano
    El número redondeado con 2 decimales
"""

numeroDecimal = float(input("Ingrese un numero decimal: "))

numeroEntero = round(numeroDecimal)
numeroEnteroCon2Decimales = round(numeroDecimal, 2)

print(f"El numero redondeado es: {numeroEntero}, y el mismo con decimales es: {numeroEnteroCon2Decimales}")