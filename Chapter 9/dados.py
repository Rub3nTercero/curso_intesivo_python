# Autor: Rubén Tercero - 04/03/2025

from random import randint

class Dado:
    
    def __init__(self, caras=6):
        self.caras = caras
        
    def tirar_dado(self):
        numero_aleatorio = randint(1, self.caras)
        return numero_aleatorio