# Autor: Rubén Tercero - 25/02/2025

pedidos_bocadillos = ["Bocadillo de jamón y queso", "Bocadillo de atún", "Bocadillo de pollo", "Bocadillo vegetal", "Bocadillo de calamares", "pastrami", "pastrami", "pastrami"]

bocadillos_terminados = []

print("No queda pastrami.")

while pedidos_bocadillos:
    bocadillo = pedidos_bocadillos.pop()
    if bocadillo != 'pastrami':
        bocadillos_terminados.append(bocadillo)
        print(f"Su {bocadillo.lower()} está listo")
    else:
        continue


print("Estos son todos los bocadillos terminados:")
for bocadillo in bocadillos_terminados:
    print(f"\t- {bocadillo}")

