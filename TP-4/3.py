"""
3. Cree un script que muestre en pantalla el perímetro de un rectángulo, leyendo su base y altura desde el teclado.
( perímetro = 2 * (base + altura)). 
"""

# Solicitar al usuario la base y la altura del rectángulo
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Calcular el perímetro
perimetro = 2 * (base + altura)

# Mostrar el resultado
print(f"El perímetro del rectángulo es: {perimetro}")