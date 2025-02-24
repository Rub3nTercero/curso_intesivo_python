# Autor: Rubén Tercero - 24/02/2025

flag = True

while flag:
    edad = input("¿Cuántos años tienes? ")
    if edad == 'quit':
        break
    
    edad = int(edad)
    
    if edad < 3:
        entrada = 'Gratuita'
    elif edad < 12:
        entrada = '8 euros'
    else:
        entrada = '12 euros'
    print(f"El precio de tu entrada es {entrada}")
    
    