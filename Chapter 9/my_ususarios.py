# Autor: Rubén Tercero - 04/03/2025

from usuarios import Usuario
from admin import Admin
 
admin = Admin('Rubén', 'Tercero Nueda', 'admin',  ["Añadir comentario", "borrar comentario", "vetar usuario"])
admin.privilegios.show_privileges()  
  
   
user_1 = Usuario("ruben", "tercero nueda", "ruternue")

user_1.incrementar_intentos_inicio()
user_1.incrementar_intentos_inicio()
user_1.incrementar_intentos_inicio()
print(f"Intentos de inicio de sesión: {user_1.intentos_inicio}")
user_1.restablecer_intentos_inicio()
print(f"Intentos de inicio de sesión: {user_1.intentos_inicio}")


user_2 = Usuario("arantxa", "donet escriva", "adonet3")

user_1.describir_usuario()
user_1.saludar_usuario()
print()
user_2.describir_usuario()
user_2.saludar_usuario()
