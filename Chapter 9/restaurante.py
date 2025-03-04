# Autor: Rubén Tercero - 04/03/2025

class Restaurante:
    
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0
        
    def describir_restaurante(self):
        print(f"Nombre Restaurante: {self.nombre_restaurante}")
        print(f"Tipo de cocina: {self.tipo_cocina}")
        print(f"Número servido: {self.numero_servido}")
        
    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto.")
        
    def establecer_numero_servido(self, clientes):
        self.numero_servido = clientes
        
    def incrementar_numero_servido(self, clientes):
        self.numero_servido += clientes

class CarritoDeHelados(Restaurante):
    
    def __init__(self, nombre_restaurante, tipo_cocina, *sabor):
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabor = sabor
    
    def mostrar_sabores(self):
        print("Tenemos los siguientes sabores:")
        for helado in self.sabor:
            print(f"\t- {helado}")
        
        
