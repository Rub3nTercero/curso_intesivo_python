# Autor: Rubén Tercero - 03/03/2025

def make_car(fabricante, modelo, **coche):
    coche['fabricante'] = fabricante.lower()
    coche['modelo'] = fabricante.lower()
    return coche

coche = make_car('subrau', 'outback', color='blue', tow_package=True)
print(coche)