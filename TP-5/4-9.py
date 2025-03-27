"""
4. Cree una función que reciba dos números como parámetro (base y exponente), y retorne el resultado de elevar base a la potencia exponente. 
"""

def potencia(base, exponente) :
    res = base ** exponente
    return res

base = int(input("Ingrese un numero: "))
exponente = int(input("Ingrese el exponente para calcular la potencia: "))

print(f"El resultado de elevar {base} a la {exponente} es {potencia(base, exponente)}.")

# Test ----------------------------------------------------------------------
def testPotencia():
    assert potencia(2, 3) == 8, "Error caso 1" # Caso 1
    assert potencia(5, 0) == 1, "Error caso 2" # Caso 2
    assert potencia(3, 2) == 9, "Error caso 3" # Caso 3

testPotencia()