# Autor Rubén Tercero - Fecha: 13/02/2025
# Este script asigna, elimina e inserta personas a una lista de invitados

invitados = ['arantxa', 'maria pombo', 'tom holland']

print(f"Hola, te invito a cenar {invitados[0].title()}.")
print(f"Hola, te invito a cenar {invitados[1].title()}.")
print(f"Hola, te invito a cenar {invitados[2].title()}.")

invitado_faltante = invitados.pop(1)
print(f"Lamentablemente, {invitado_faltante.title()} no podra venir.")

invitados.append("max")
print(f"Hola, te invito a cenar {invitados[-1].title()}.")

print("Hola, he encontrado una mesa más grande.")

invitados.insert(0, "tara")
invitados.insert(int(len(invitados)/2), "willy")
invitados.append("willy wonka")

for nombre in invitados:
    print(f"Hola, {nombre.title()} te invito a la nueva fiesta. ¡Espero que te guste!")

while len(invitados)>2:
    nombre=invitados.pop()
    print(f"Lo siento, {nombre.title()} pero no puedo invitarte a la fiesta.")
    
print(f"Hola, {invitados[0].title()} sigues invitado a mi fiesta.")
print(f"Hola, {invitados[1].title()} sigues invitado a mi fiesta.")
print(f"Total de invitados: {len(invitados)}")

del(invitados)
