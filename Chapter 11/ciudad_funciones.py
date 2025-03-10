# Autor: Rubén Tercero - 10/03/2025

def ciudad_pais(ciudad, pais, habitantes=""):
    if habitantes == "":
        resultado = f"{ciudad.title()}, {pais.title()}"
    else:    
        resultado = f"{ciudad.title()}, {pais.title()} - habitantes={habitantes}"
    return resultado

resultado = ciudad_pais("valencia", "españa", 500000)
print(resultado)