"""
3. Cree un script que le solicite al usuario ingresar dos números por teclado, y
luego indique por pantalla cuál de ellos es el mayor. Contemple la posibilidad
de que los números sean iguales, y muestre un mensaje acorde.
"""

num1 = input("Ingrese un numero: ")
num2 = input("Ingrese otro numero: ")

def compararNumeros(num1, num2) :
    if (num1 > num2) :
        print(f"El numero {num1} es mayor que {num2}")
    elif (num2 > num1) :
        print(f"El numero {num2} es mayor que {num1}")
    else :
        print(f"Ambos numeros son iguales!")

compararNumeros(num1, num2)