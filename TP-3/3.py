"""
Cree un script que almacene, en dos variables, una base y un exponente, y luego muestre en pantalla 
el resultado de elevar el número base a la potencia exponente.
"""

base = input("Ingrese un numero (base de la potencia): ")
exponente = input("Ingrese un numero (exponente de la potencia): ")

resultado = int(base) ** int(exponente)

print(f"El resultado de elevar {base} a la potencia {exponente} es: {str(resultado)}")