# Autor: Rubén Tercero - 03/03/2025

def mostrar_mensaje():
    print("Hola, Mundo!")

def mostrar_mensajes(mensajes):
    for mensaje in mensajes:
        print(mensaje)

def enviar_mensajes(mensajes_espera, mensajes_enviados):
    while mensajes_espera:
        mensaje = mensajes_espera.pop()
        print(mensaje)
        mensajes_enviados.append(mensaje)
    return mensajes_espera, mensajes_enviados
        

# mostrar_mensaje()
mensajes = ['hola Mundo', 'Python es vida', 'Ojos que no ven']
nuevos_mensajes = mensajes[:]

mensajes_espera, mensajes_enviados = enviar_mensajes(nuevos_mensajes, [])
print(f"Mensajes a la espera: {mensajes_espera}")
print(f"Mensajes enviados: {mensajes_enviados}")
print(f"Mensajes originales: {mensajes}")