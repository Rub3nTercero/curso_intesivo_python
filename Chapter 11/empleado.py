# Autor: Rubén Tercero - 10/03/2025

class Empleado:
    
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre.title()
        self.apellido = apellido.title()
        self.salario = int(salario)
        
    def dar_aumento(self, subida=5000):
        self.salario += subida

empleado = Empleado("ruben", "tercero", 24000)
empleado.dar_aumento()
print(f"Salario: {empleado.salario}")
        
    
     