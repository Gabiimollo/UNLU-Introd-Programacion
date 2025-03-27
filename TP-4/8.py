"""
8. Cree un script que le solicite al usuario una temperatura en grados Celsius y conviértela a Fahrenheit.
"""

gradosCelsius = float(input("Ingrese los grados en Celsius: "))

gradosFahrenheit = (gradosCelsius * 1.8) + 32.0

print(f"Los grados Celsius {gradosCelsius}°C expresados en Fahrenheit son {gradosFahrenheit}°F")