"""
6. Implemente un algoritmo que intercambie los valores entre dos variables a y b cualesquiera. Por ejemplo, 
si a = 10 y b = 5, # luego de ejecutar el algoritmo, la variable a debería ser igual 5, y 
la variable b debería ser igual a 10.
"""

nro1 = input("Ingrese un numero: ")
nro2 = input("Ingrese otro numero: ")

print(f"Los valores iniciales son: a = {nro1} y b = {nro2}")

aux = nro1
nro1 = nro2
nro2 = aux

print(f"Los valores finales son: a = {nro1} y b = {nro2}")

# ----------------------------------------------------------------------------------------------------------- #

"""
7. En Python es posible resolver el problema del intercambio de valores sin hacer uso de variables 
adicionales, mediante la sintaxis de asignación múltiple. Investigue de qué se trata dicha funcionalidad, 
y utilízala para resolver el ejercicio anterior sin utilizar variables auxiliares/adicionales.
"""

nro1bis = input("Ingrese un numero: ")
nro2bis = input("Ingrese otro numero: ")

print(f"Los valores iniciales son: a = {nro1bis} y b = {nro2bis}")

nro1bis, nro2bis = nro2bis, nro1bis

print(f"Los valores finales son: a = {nro1bis} y b = {nro1bis}")

# ----------------------------------------------------------------------------------------------------------- #

"""
7.2 Otra forma de hacerlo
"""
num_1 = input("Ingrese un numero: ")
num_2 = input("Ingrese otro numero: ")

print(f"Los valores iniciales son: a = {num_1} y b = {num_2}")

num_1 = int(num_1) + int(num_2)
num_2 = num_1 - int(num_2)
num_1 = num_1 - int(num_2)

print(f"Los valores finales son: a = {num_1} y b = {num_2}")