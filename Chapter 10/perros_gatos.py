# Autor: Rubén Tercero - 06/03/2025

from pathlib import Path


def archivo_encontrado(path):
    try:
        content = path.read_text(encoding='UTF-8')
    except FileNotFoundError:
        pass
    # print("No hemos encontrado los archivos. ¡Revisa las rutas!")
    else:
        return content

perros = Path('Chapter 10\\perrs.txt')
gatos = Path('Chapter 10\\gatos.txt')

content_perros = archivo_encontrado(perros)
content_gatos = archivo_encontrado(gatos)

if content_perros:
    print("El archivo de perros dice lo siguiente:")
    print(content_perros)

if content_gatos:
    print("El archivo de gatos dice lo siguiente:")
    print(content_gatos)
