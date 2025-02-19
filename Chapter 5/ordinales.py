# Autor Rubén Tercero - Fecha: 19/02/2025
# Este script nombra los números ordinales

numeros = [numero for numero in range(1, 10)]
texto = ""

for numero in numeros:
    if numero == 1:
        ordinal = f'{numero}st'
    elif numero == 2:
        ordinal = f'{numero}nd'
    elif numero == 3:
        ordinal = f'{numero}rd'
    else:
        ordinal = f'{numero}th'
    texto = texto + ordinal + " "

print(texto)