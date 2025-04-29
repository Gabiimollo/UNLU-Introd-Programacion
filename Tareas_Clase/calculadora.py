"""
Diseñar una calculadora en python con las funciones de suma, resta, multiplicación, division, 
potencia
"""
def calculadora(num1, num2, operacion) :
    res = ""

    if (operacion == "Suma" or operacion == "1") :
        res = num1 + num2

    elif (operacion == "Resta" or operacion == "2") :
        res = num1 - num2

    elif (operacion == "Multiplicación" or operacion == "3") :
        res = num1 * num2

    elif (operacion == "División" or operacion == "4") :
        if (num2 != 0) :
            res = num1 / num2
        else :
            print("El denominador (numero 2) no puede ser 0")

    elif (operacion == "Potencia" or operacion == "5") :
        res = num1 ** num2
    else :
        print("Seleccione la opción correcta")

    return res

num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))

operacion = input("1 - Suma \n2 - Resta \n3 - Multiplicación \n4 - División \n5 - Potencia \n Ingrese una opción para operar: ")

print(f"El resultado es: {calculadora(num1, num2, operacion)}")