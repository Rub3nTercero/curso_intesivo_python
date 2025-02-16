# Autor Rubén Tercero - Fecha: 16/02/2025
# Este script recorre una lista de elementos a partir de un bucle 'for'

animales = ['perro', 'gato', 'conejo', 'rana', 'pez', 'hamster']

for animal in animales:
    print(f"Un {animal} sería una excelente mascota")
    
print("¡Cualquiera de estos animales sería una excelente mascota!")

print("Estos son los tres primeros elementos de la lista:")
for animal in animales[:3]:
    print(animal)

print("Estos tres elementos están en el medio de la lista:")
for animal in animales[int(len(animales)/2)-1 : int((len(animales)/2) + 2)]:
    print(animal)

print("Estos son los tres últimos elementos de la lista:")
for animal in animales[-3:]:
    print(animal)