# Autor Rubén Tercero - Fecha: 19/02/2025
# Este script describe la etapa vital de una persona según su edad

edad = 25

if edad < 2:
    persona = 'bebe'
elif edad < 4:
    persona = 'niño pequeño'
elif edad < 13:
    persona = 'niño'
elif edad < 20:
    persona = 'adolescente'
elif edad < 65:
    persona = 'adulto'
else:
    persona = 'abualo'

print(f"La persona es un {persona}.")