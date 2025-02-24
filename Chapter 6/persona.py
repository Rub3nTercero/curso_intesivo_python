# Autor Rubén Tercero - Fecha: 20/02/2025
# Este script describe a una persona con el uso de los diccionarios

persona = {
    'nombre': 'Arantxa',
    'apellido': 'Donet Escriva',
    'edad': 24,
    'ciudad': 'piles',
}

nombre = persona.get('nombre')
apellido = persona.get('apellido')
edad = persona.get('edad')
ciudad = persona.get('ciudad')

print(nombre.title())
print(apellido.title())
print(edad)
print(ciudad.title())
print("\n")

persona_1 = {
    'nombre': 'Jaume',
    'apellido': 'Belda',
    'edad': 24,
    'ciudad': 'piles',
}

persona_2 = {
    'nombre': 'Alex',
    'apellido': 'Rodriguez San martin',
    'edad': 25,
    'ciudad': 'oliva',
}

personas = [persona, persona_1, persona_2]

for persona in personas:
    for k, v in persona.items():
        print(f"{k}:{v}")
    print("\n")
        