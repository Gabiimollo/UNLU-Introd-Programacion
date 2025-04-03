"""
10. Genere un programa que permita al usuario ingresar los coeficientes de una función 
cuadrática ax2+bx+c y de como resultado las raíces de la función.
"""

coef_a = int(input("Ingrese el coeficiente a: "))
coef_b = int(input("Ingrese el coeficiente b: "))
coef_c = int(input("Ingrese el coeficiente c: "))

def raicesFuncion(a, b, c) :
    raizPositiva = ((-b) + (((b**2) - (4*a*c)) ** (1/2)))/(2*a)
    raizNegativa = ((-b) - (((b**2) - (4*a*c)) ** (1/2)))/(2*a)
    return raizPositiva, raizNegativa

print(raicesFuncion(coef_a, coef_b, coef_c))

