# Autor Rubén Tercero - Fecha: 19/02/2025
# Este script realiza un condicional if-else
import random

puntos = 0
color = ['rojo', 'amarillo', 'verde']

color_alien = random.choice(color)
print("COLOR: " + color_alien)

if color_alien == 'verde':
    puntos = 5
elif color_alien == 'amarillo':
    puntos = 10
else:
    puntos = 15
    
print(f"¡Has ganado {puntos} puntos!")


