# Autor: Rubén Tercero - 05/03/2025

from pathlib import Path

path = Path('libro_invitados.txt')
lista_invitados = ''
flag = True

while flag:
    invitado = input('Escribe tu nombre de usuario: ')
    if invitado == 'q':
        flag = False
    else:
        lista_invitados = lista_invitados + invitado + '\n'

path.write_text(lista_invitados.strip())
