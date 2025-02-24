# Autor: Rubén Tercero - 24/02/2025
# Este script comprueba si un número es múltiplo de 10

numero = input("Introduce un número: ")
numero = int(numero)

if numero % 10 == 0:
    print(f"El {numero} es múltiplo de 10.")
else:
    print(f"El {numero} no es múltiplo de 10.")