# Autor: Rubén Tercero - 06/03/2025

while True:
    
    numero_1 = input("Primer Número: ")
    if numero_1 == 'q':
        print("¡Adiós!")
        break
    
    numero_2 = input("Segundo Número: ")
    if numero_2 == 'q':
        print("¡Adiós!")
        break
    try:
        suma = int(numero_1) + int(numero_2)
    except ValueError:
        print("Debes escribir numeros para hacer la suma.")
    else:
        print(f"El valor de la suma es {suma}")
        
    
     