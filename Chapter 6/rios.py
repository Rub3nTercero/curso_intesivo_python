# Autor Rubén Tercero - Fecha: 24/02/2025
# Este script describe el funcionamiento de bucles en diccionarios

rios = {
    'nilo': 'egipto',
    'misisipi': 'estados unidos',
    'yangtsé': 'china',
}

for rio, pais in rios.items():
    print(f"El {rio.title()} discurre por {pais.title()}.")

for rio in rios:    # rios.keys()
    print(rio.title())

for pais in rios.values():
    print(pais.title())
