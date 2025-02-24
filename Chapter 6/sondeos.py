# Autor Rubén Tercero - Fecha: 24/02/2025
# Este script describe el sonde de los lenguajes de programacion favoritos de algunas personas

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phill': 'python',
    'ruben': 'python',
    'sergi': 'javascript',
}

personas = ['ruben', 'arantxa', 'roman', 'sergi', 'sarah']

personas_encuestas = [persona_encuestas.lower() for persona_encuestas in favorite_languages.keys()]

for persona in personas:
    if persona.lower() in personas_encuestas:
        print(f"{persona.title()}, gracias por responder.")
    else:
        print(f"{persona.title()}, debes hacer la encuesta.")