# Autor: Rubén Tercero - 05/03/2025

from pathlib import Path

invitado = input('Escribe tu nombre de usuario: ')

path = Path('invitado.txt')
path.write_text(invitado)
