"""
4. Un colega programador nos ha proporcionado un script que resuelve la multiplicación de dos 
números y muestra el resultado en pantalla; el contenido del script es el siguiente: 
"""

numero1 = 10 # Es una variable
numero2 = 5  # Es otra variable

resultado = numero1 * numero2 # Es una variable que almacena el resultado de la operación

print('El producto entre ' + str(numero1) + ' y ' + str(numero2) + ' da ' + str(resultado))

"""
Ejecute el código para verificar el funcionamiento del script, y luego analice detenidamente el 
código y responda: 
    - ¿Qué son numero1, numero2, y resultado? 
    - ¿Por qué es necesario utilizar la función str(...) para mostrar en pantalla los valores de 
       numero1, numero2, y resultado? 

       Se debe utilizar str(...) ya que Python solo concatena valores del tipo String entre sí, o 
       suma valores numericos con el operador +. Al estar trabajando con numeros, necesito castearlos
       como strings con str(...) para poder concatenarlos y mostrarlos por consola.
"""