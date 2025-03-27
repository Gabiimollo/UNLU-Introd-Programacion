"""
3. Cree una función que reciba un string como parámetro, y retorne la cantidad de letras que posee. Luego, utilice la función para escribir un programa que solicite ingresar el nombre del usuario, y luego muestre en pantalla cuántas letras tiene ese nombre. 
"""

def contarLetrasPalabra(palabra) :
    letrasPalabra = len(palabra)
    return letrasPalabra

palabra = input("Ingrese una palabra: ")

print(f"La palabra '{palabra}' tiene {contarLetrasPalabra(palabra)} letras")