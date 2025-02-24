# Autor: Rubén Tercero - 24/02/2025
# Este script pregunta cuantas personas vendran a cenar en un restaurante

personas = input("¿Cuántos vienen a cenar? ")
personas = int(personas)

if personas > 8:
    print("Deben esperar hasta que tengamos una mesa disponible.")
else:
    print("La mesa está lista.")