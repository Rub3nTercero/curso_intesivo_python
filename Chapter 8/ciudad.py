# Autor: Rubén Tercero - 03/03/2025

def describir_ciudad(ciudad, pais="España"):
    print(f"{ciudad.title()} está en {pais.title()}")
    
def ciudad_pais(ciudad, pais):
    return f"{ciudad.title()}, {pais.title()}"
    
describir_ciudad("madrid")
describir_ciudad("valencia")
describir_ciudad("reikiavik", pais="finlandia")

localizacion_0 = ciudad_pais("santiago", "chile")
localizacion_1 = ciudad_pais("londres", "reino unido")
localizacion_2 = ciudad_pais("valencia", "españa")

print(localizacion_0)
print(localizacion_1)
print(localizacion_2)