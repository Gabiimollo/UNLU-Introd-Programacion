"""
1. Cree un script que, al ejecutarlo, le solicite al usuario ingresar su nombre de pila, luego lo 
salude y calcule la cantidad de letras del nombre, mostrando el mensaje “Hola, [NOMBRE], tu nombre 
tiene [N] letras.”.
"""

# Solicito al usuario su nombre de pila
nombre_usuario = input("Ingrese su nombre de pila: ")

# Calculo cantidad de letras
cantidad_letras = len(nombre_usuario)

# Muestro el resultado
print(f"Hola {nombre_usuario}, tu nombre tiene {cantidad_letras} letras")