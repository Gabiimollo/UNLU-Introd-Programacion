# 5. Cree un script llamado mi_nombre.py, el cual almacene su nombre completo en una variable, y luego lo muestre en pantalla.
# 6. Modifique el código del ejercicio anterior para que el nombre se almacene en una variable, y el apellido en otra. Además, introduzca una tercera variable para almacenar su edad. Ahora, en pantalla muestre el mensaje “Mi nombre completo es [NOMBRE] [APELLIDO] y tengo [EDAD] años.”. 

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))

print("Mi nombre es " + nombre + " " + apellido + " y tengo " + str(edad) + " años.")
print(f"Mi nombre es {nombre} {apellido} y tengo {str(edad)} años.")