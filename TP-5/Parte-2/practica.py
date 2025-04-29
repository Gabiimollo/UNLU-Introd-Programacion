from mis_funciones import sumarCifras, sueldos

def main() :
    # --------------------------------- Suma de Cifras --------------------------------- #

    numero = int(input("Ingrese un numero de 4 cifras: "))

    print(f"La suma de los digitos del numero {numero} es {sumarCifras(numero)}")

    # ---------------------------------------------------------------------------------- #
    # -------------------------------- Calculo Salario --------------------------------- #
    
    cantidadVentas = int(input("Ingrese la cantidad de ventas del vendedor: "))
    valorTotalVentas = int(input("Ingrese el monto total de ventas del vendedor: "))

    print(f"El sueldo mensual del vendedor es {sueldos(cantidadVentas, valorTotalVentas)}")
    
    # ---------------------------------------------------------------------------------- #  
    # -------------------------------- Calculo Salario --------------------------------- #
main()