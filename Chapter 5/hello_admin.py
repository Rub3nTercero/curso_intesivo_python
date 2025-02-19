# Autor Rubén Tercero - Fecha: 19/02/2025
# Este script recorre una lista de usuarios para buscar un elemento

usuarios = ['ruben', 'roman', 'emil', 'arantxa', 'admin']

# usuarios = usuarios.clear()

if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print(f"Hola, {usuario}, ¿quieres ver un informe de estado?")
        else:
            print(f"Hola, {usuario.title()}, gracias por volver a entrar.")
else:
    print("¡Necesitamos encontrar algún usuario!")