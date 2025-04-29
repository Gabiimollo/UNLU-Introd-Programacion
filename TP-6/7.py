"""
7. Cree un script que determine si un triángulo es isósceles, equilátero, o escaleno. 
Para determinar esto, se le solicitará al usuario ingresar tres números, correspondientes 
a los tres lados del triángulo.

equilátero = todos los lados iguales
isósceles = dos lados iguales
escaleno = todos los lados diferentes
"""

def tipoTriangulo(lado1, lado2, lado3) :
    res = ""

    if (lado1 == lado2 == lado3) :
        res = "Equilátero"
    elif(lado1 == lado2 or lado2 == lado3 or lado1 == lado3) :
        res = "Isóceles"
    else :
        res = "Escaleno"
    
    return res

lado1 = float(input("Ingrese el lado 1: ")) 
lado2 = float(input("Ingrese el lado 2: "))
lado3 = float(input("Ingrese el lado 3: ")) 

print(f"{tipoTriangulo(lado1, lado2, lado3)}")

def tipoTrianguloBIS(lado1, lado2, lado3) :
    res = ""

    if (lado1 == lado2 and lado1 == lado3) :
        res = "Equilatero"
    elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3) :
        res = "Isóceles"
    else :
        res = "Escaleno"
    
    return res
    

