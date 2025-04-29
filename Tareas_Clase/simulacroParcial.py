def mayorEdad(edad1, edad2, edad3) :
    mayor = ""

    if (edad1 == edad2 and edad2 == edad3) :
        mayor = "Son iguales"
    elif (edad1 > edad2 and edad1 > edad3) :
        mayor = edad1
    elif (edad2 > edad3) :
        mayor = edad2
    else :
        mayor = edad3

    return mayor

def test_mayorEdad() :
    assert mayorEdad(10, 20, 30) == 30, "Error caso 1"
    assert mayorEdad(20, 30, 10) == 30, "Error caso 2"
    assert mayorEdad(30, 10, 20) == 30, "Error caso 3"
    assert mayorEdad(20, 10, 20) == 20, "Error caso 4"
    assert mayorEdad(30, 20, 20) == 30, "Error caso 5"
    assert mayorEdad(10, 20, 20) == 20, "Error caso 6"
    assert mayorEdad(20, 20, 20) == "Son iguales", "Error caso 7"
    assert mayorEdad(10, 20, 10) == 20, "Error caso 8"
    print("Pasó")
    
test_mayorEdad();


def piedraPapelTijera(jugador1, jugador2) :
    ganador = ""

    if(jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "tijera" and jugador2 == "papel") or (jugador1 == "papel" and jugador2 == "piedra") :
        ganador = f"Jugador 1 gana con {jugador1}"
    elif(jugador1 == jugador2) :
        ganador = "Empate"
    else :
        ganador = f"Jugador 2 gana con {jugador2}"

    return ganador

def test_piedraPapelTijera() :
    assert piedraPapelTijera("piedra", "papel") == "Jugador 2 gana con papel", "Error caso 1" 
    assert piedraPapelTijera("piedra", "tijera") == "Jugador 1 gana con piedra", "Error caso 2" 
    assert piedraPapelTijera("piedra", "piedra") == "Empate", "Error caso 3" 

    assert piedraPapelTijera("papel", "tijera") == "Jugador 2 gana con tijera", "Error caso 4" 
    assert piedraPapelTijera("papel", "piedra") == "Jugador 1 gana con papel", "Error caso 5" 
    assert piedraPapelTijera("papel", "papel") == "Empate", "Error caso 6" 

    assert piedraPapelTijera("tijera", "piedra") == "Jugador 2 gana con piedra", "Error caso 7" 
    assert piedraPapelTijera("tijera", "papel") == "Jugador 1 gana con tijera", "Error caso 8" 
    assert piedraPapelTijera("tijera", "tijera") == "Empate", "Error caso 9" 

    print("Pasó")

test_piedraPapelTijera()