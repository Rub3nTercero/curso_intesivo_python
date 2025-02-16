# Autor Rubén Tercero - Fecha: 16/02/2025
# Este script recorre una lista de elementos a partir de un bucle 'for'

pizzas = ['4 quesos', 'reina', 'caprichosa']

for pizza in pizzas:
    print(f"Me gusta la pizza de {pizza}.")

print("¡Me encanta la pizza!")

friend_pizzas = pizzas[:]

pizzas.append('champiñon')
friend_pizzas.append('vegetariana')

print("Mis pizzas favoritas son:")
for pizza in pizzas:
    print(pizza)

print("Las pizzas favoritas de mi amigo son:")
for pizza in friend_pizzas:
    print(pizza)
    