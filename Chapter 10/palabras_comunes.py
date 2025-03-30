# Autor: Rubén Tercero - 06/03/2025

from pathlib import Path

path = Path('Chapter 10\\DonQuijote.txt')

try:
    content = path.read_text(encoding='UTF-8')
except FileNotFoundError:
    print(f"Revisa las rutas del archivo: {path}")
else:
    palabra = 'quijote'
    palabra_veces = content.lower().count(palabra)
    print(f'La palabra "{palabra}" aparece un total de {palabra_veces}')