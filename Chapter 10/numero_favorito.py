# Autor: Rubén Tercero - 06/03/2025

from pathlib import Path
import json

path = Path('numbers.json')

while True:
    numero = input("Introduce tu número favorito: ")

    if numero == 'q':
        print("¡Adiós!")
        break

    try:
        numero = int(numero)  
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue
    else:
        
        if path.exists():
            content = path.read_text(encoding='UTF-8')
            numero_guardado = json.loads(content)

            if numero == numero_guardado:
                print(f"¡Sé cuál es tu número favorito! Es el {numero_guardado}")
            else:
                print(f"Has cambiado tu número favorito a {numero}.")
                path.write_text(json.dumps(numero))
        else:
            path.write_text(json.dumps(numero))
            print(f"Tu número favorito {numero} ha sido guardado.")

        
                