"""
11.  Genere un programa que solicite al usuario una cantidad de segundos, 
e imprima el tiempo en el formato HH:MM:SS.
"""

segundos = int(input("Ingrese la cantidad de segundos: "))

HH = (segundos//3600)
MM = (segundos%3600)//60 # El modulo se utiliza para extraer lo que me "sobra" para colocar en los segundos
SS = segundos%60

print(f"{HH}:{MM}:{SS}")