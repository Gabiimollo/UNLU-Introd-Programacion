"""
6. Cree un script que lea dos números de teclado (una base y un exponente) y luego muestre en pantalla el resultado 
de elevar el número base a la potencia exponente.
"""

# Leer la base y el exponente desde el teclado
base = float(input("Ingrese la base: "))
exponente = float(input("Ingrese el exponente: "))

# Calcular la potencia
resultado = base ** exponente

# Mostrar el resultado
print(f"El resultado de {base} elevado a la potencia {exponente} es: {resultado}")