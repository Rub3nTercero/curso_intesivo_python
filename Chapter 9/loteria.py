# Autor: Rubén Tercero - 04/03/2025

from random import choice

class Loteria:
    
    def __init__(self):
        self.loteria = [1,2,3,4,5,6,7,8,9,0,'A','B','C','D','E']
        self.numero_premiado = ''
        self.boleto = ''
        self.contador = 0

        
    def empezar_loteria(self):
        for numero in range(5):
            numero = choice(self.loteria)
            self.numero_premiado += str(numero) 
        print(f"El número premiado es: {self.numero_premiado}")
    
    def comprobar_numero(self, boleto):
        if self.numero_premiado == boleto:
            print(f"El número {boleto} ha sido premiado!!")
        else:
            print(f"El número {boleto} no ha sido premiado.")
    
    def probabilidad_loteria(self):
        while self.numero_premiado != self.boleto:
            self.boleto = ''
            for numero in range(5):
                numero = choice(self.loteria)
                self.boleto += str(numero)
            self.contador += 1
        return self.contador