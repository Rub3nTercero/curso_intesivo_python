# Autor: Rubén Tercero - 24/02/2025

flag = True

while flag:
    ingrediente = input("Introduce el ingrediente que desees añadir a tu pizza: ")
    if ingrediente == "quit":
        flag = False
    else:
        print(f"Añadiré {ingrediente.title()} a tu pizza.")
        