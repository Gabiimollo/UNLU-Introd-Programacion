""" 
8. Se le ha solicitado a dos programadores que resuelvan el mismo problema: 
conociendo el total de inscriptos de una asignatura y cuántos alumnos han asistido a la clase de hoy, 
queremos un programa que nos muestre en pantalla el porcentaje de asistencia del día de hoy. 
Las dos versiones que realizaron los programadores son:  
"""
### Programador A----------------------------------------------------------------
# almaceno cuántos alumnos asistieron a la clase de hoy
alumnos_presentes = 35

# almaceno el total de inscriptos en la asignatura
alumnos_inscriptos = 54

# calculo del porcentaje de alumnos presentes en la clase de hoy
porcentaje_presentes = (alumnos_presentes * 100) / alumnos_inscriptos

# muestro el porcentaje de alumnos presentes en pantalla
print("Hoy asistió el " + str(porcentaje_presentes) + " porcentaje del alumnado.")

### ------------------------------------------------------------------------------
### Programador B ----------------------------------------------------------------

p = 35
i = 54
pp = (p * 100) / i
print("Hoy asistió el " + str(pp) + " porcentaje del alumnado.")

### ------------------------------------------------------------------------------

"""
Analice detenidamente ambas versiones, y luego responda: 
- ¿Ambas versiones resuelven el problema?. 
- ¿Cuál versión es más legible y fácil de comprender?. 
- ¿Qué desventajas tiene escribir código en la forma en que lo hace el Programador B?.


Si ambas versiones resuelven el problema.
La version A es la mas legible dado que está comentado y las variables poseen etiquetas que indican claramente lo que almacenará
La version B es menos legible y dificulta la comprensión del código, ya que las variables no poseen etiquetas que indiquen su función.
"""