# Autor: Rubén Tercero - 05/03/2025

from pathlib import Path

# Ejercicio 1
path = Path('Chapter 10/aprender_python.txt')
print(path.read_text())

contents_C = ''
for line in path.read_text().splitlines():
    contents_C = contents_C + line.replace('Python', 'C') + '\n'
print(contents_C)