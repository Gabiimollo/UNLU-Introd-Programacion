"""
1. Diseña una función que calcule y retorne la suma de las cifras de un número entero positivo 
de 4 cifras. 
"""

def sumarCifras(numero) :

    unidadMil = numero // 1000
    centena = (numero % 1000) // 100
    decena = (numero % 100) // 10
    unidad = numero % 10

    sumaCifras = unidad + decena + centena + unidadMil

    return sumaCifras

"""
Una empresa de ventas de Alemania paga a sus empleados un salario fijo de 5000 euros, más una 
comisión de 200 euros por cada venta realizada, más el 8 % del valor de esas ventas. 

Diseña una función que calcule y devuelva el sueldo correspondiente en un mes determinado, 
recibiendo la cantidad de ventas realizadas por un empleado y el valor total de las mismas.
"""

def sueldos(cantidadVentas, valorTotalVentas) :
    sueldoFijo = 5000
    comisionVenta = 200 * cantidadVentas
    extraValorVenta = (valorTotalVentas * 8)/100

    sueldo = sueldoFijo + comisionVenta + extraValorVenta

    return sueldo