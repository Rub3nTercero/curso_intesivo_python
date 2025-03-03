# Autor: Rubén Tercero - 03/03/2025

def sandwich(*ingredientes):
    print("Estos son los ingredientes para el sandwich")
    for ingrediente in ingredientes:
        print(f"\t- {ingrediente}")

sandwich("Espinacas", "trufa", "Jamon york")
sandwich("Pollo")
sandwich("Queso", "trufa", "champiñones", "jamon serrano")