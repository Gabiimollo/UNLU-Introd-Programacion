"""
Cree un script que, sabiendo cuántos pesos argentinos tiene una persona ahorrada en su cuenta 
(almacenando ese monto en una variable), muestre en pantalla los montos convertidos en dólares 
(U$1 = $80.5), reales ($R1 = $14.1), y euros (€1 = $69.5). La salida del programa debe tener el 
siguiente formato:

Usted tiene $XXX pesos argentinos, los cuales se convierten en:
- U$XXX dólares.
- R$XXX reales.
- €XXX euros.

"""

total_ars = int(input("Ingrese el monto de sus ahorros en AR$: "))

tipo_cambio_USD = 80.5
tipo_cambio_BRL = 14.1
tipo_cambio_EUR = 69.5

print(f"Usted tiene ${total_ars} pesos argentinos, los cuales se convierten en: \n - U${round(total_ars / tipo_cambio_USD, 2)} dólares \n - R${round(total_ars / tipo_cambio_BRL, 2)} reales. \n - €{round(total_ars / tipo_cambio_EUR, 2)} euros.")