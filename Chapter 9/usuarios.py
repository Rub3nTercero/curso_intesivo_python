# Autor: Rubén Tercero - 04/03/2025

class Usuario:
    
    def __init__(self, nombre, apellidos, nickname):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nickname = nickname
        self.intentos_inicio = 0
        
    def describir_usuario(self):
        print(f"Nombre: {self.nombre.title()}")
        print(f"Apellidos: {self.apellidos.title()}")
        print(f"Nickname: {self.nickname}")
        
    def saludar_usuario(self):
        print(f"Hola, {self.nickname}!")
        
    def incrementar_intentos_inicio(self):
        self.intentos_inicio+=1
        
    def restablecer_intentos_inicio(self):
        self.intentos_inicio = 0
        

        
