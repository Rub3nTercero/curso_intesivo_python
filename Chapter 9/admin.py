# Autor: Rubén Tercero - 04/03/2025

from usuarios import Usuario

class Privilegios:

    def __init__(self, privilegios):
        self.privilegios = privilegios
        
    def show_privileges(self):
        print("Estos son los privilegios del Admin:")
        for privilegio in self.privilegios:
            print(f"\t- {privilegio}")
        
class Admin(Usuario):
    
    def __init__(self, nombre, apellidos, nickname, privilegios):
        super().__init__(nombre, apellidos, nickname)
        self.privilegios = Privilegios(privilegios)