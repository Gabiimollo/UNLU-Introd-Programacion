"""
4. Cree un script que le solicite al usuario ingresar un número por teclado, y le
informe con un mensaje si su número es positivo, negativo, o 0.
"""

num = float(input("Ingrese un numero: "))

def positivoNegativoCero(num) :
    if (num > 0) :
        print(f"El numero {num} es positivo")
    elif (num < 0) :
        print(f"El numero {num} es negativo")
    else :
        print(f"El numero es cero")

positivoNegativoCero(num)