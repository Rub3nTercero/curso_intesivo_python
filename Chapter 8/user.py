# Autor: Rubén Tercero - 03/03/2025

def build_profile(nombre, apellido, **user):
    user['nombre'] = nombre.title()
    user['apellido'] = apellido.title()
    return user

user = build_profile("ruben", "tercero", nickname="ruternue")

print(user)