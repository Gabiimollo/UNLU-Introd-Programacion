"""
1. Cree un script que le solicite al usuario ingresar un número por teclado, y luego le informe 
en pantalla si su número es mayor que 10; antes de finalizar e independientemente de lo que haya 
sucedido antes, el script mostrará un mensaje de despedida.
"""

numUser = float(input("Ingrese un numero: "))

def mayorQue10(numUser) :
    if (numUser > 10) :
        print(f"Tu número {numUser} es mayor que 10!")
        print("Saludos!")
    else :
        print("Saludos!")

mayorQue10(numUser)

"""
2. Modifique el script anterior para que mantenga el funcionamiento, pero ahora, cuando el 
número no es mayor que 10, también se muestre un mensaje “Tu número (N) es menor o igual 
que 10!”.
"""

numUser = float(input("Ingrese un numero: "))

def mayorQue10Bis(numUser) :
    if (numUser > 10) :
        print(f"Tu numero {numUser} es mayor que 10!")
    else :
        print(f"Tu numero {numUser} es menor o igual a 10!")
        
    print("Saludos!");

mayorQue10Bis(numUser);