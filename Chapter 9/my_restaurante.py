# Autor: Rubén Tercero - 04/03/2025

from restaurante import Restaurante, CarritoDeHelados


restaurante_1 = CarritoDeHelados("R3N", "Hamburguesería", "vainilla", "chocolate", "fresa")

restaurante_1.numero_servido = 3
restaurante_1.establecer_numero_servido(4)
restaurante_1.incrementar_numero_servido(2)
restaurante_1.describir_restaurante()
restaurante_1.mostrar_sabores()

restaurante_2 = Restaurante("Goku", "Italiano")
restaurante_3 = Restaurante("Bobo", "Chino")

restaurante_2.describir_restaurante()
restaurante_3.describir_restaurante()
