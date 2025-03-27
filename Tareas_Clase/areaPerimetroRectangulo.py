# Ingresar por teclado los lados de un rectangulo e imprimir el area y el perimetro

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"El área del rectangulo es: {area} y el perimetro es: {perimetro}")

# -------------------------------------------------------------------------- #

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

print(f"El área del rectangulo es {base * altura} y el perimetro es {2 * (base + altura)}")

# Esta manera nos permite ahorrar espacio en memoria al no declarar ni almacenar las variables "area" y "perimetro"
# pero el código se vuelve menos claro.

# Es importante dejar comentarios para mejorar la legibilidad del codigo que estamos creando. 
# Comentar ---> SUMA EN EL PARCIAL (Buena práctica)