"""
1. Cree una función que reciba dos números como parámetro, y muestre en pantalla la suma aritmética de ambos. Invoque a la función con dos números leídos desde teclado. 
2. Modifique el script del ejercicio anterior para que la función retorne el resultado en vez de mostrarlo. El programa debe seguir mostrando el resultado en pantalla. 
"""

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

def sumaDosNumeros(num1, num2) :
    res = num1 + num2
    return res

print(f"El resultado es: {sumaDosNumeros(num1, num2)}")