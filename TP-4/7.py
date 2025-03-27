"""
7. Cree un script que solicite al usuario ingresar una cantidad de horas, y luego muestre por pantalla la conversión de esas horas a minutos y segundos. 
"""

horas = int(input("Ingrese la cantidad de horas: "))

minutos = (horas * 60)
segundos = (horas * 3600)

print(f"La cantidad de horas {horas} expresado en minutos es {minutos} y en segundos es {segundos}")