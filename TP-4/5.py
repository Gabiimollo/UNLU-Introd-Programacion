"""
5. Cree un script que le solicite a un alumno ingresar su apellido, la nota del primer parcial, y la nota del 
segundo parcial. Finalmente, se debe mostrar un reporte con la siguiente información:
"""

# Solicitar datos al alumno
apellido = input("Ingrese su apellido: ")
nota_parcial_1 = float(input("Ingrese la nota del primer parcial: "))
nota_parcial_2 = float(input("Ingrese la nota del segundo parcial: "))

# Calcular el promedio
promedio = (nota_parcial_1 + nota_parcial_2) / 2

# Mostrar el reporte
print(f"\n--- Reporte --- \n - Apellido del alumno: {apellido} \n - Nota del primer parcial: {nota_parcial_1} \n - Nota del segundo parcial: {nota_parcial_2} \n - Promedio: {promedio}")