# Autor: Rubén Tercero - 03/03/2025

def hacer_album(nombre, titulo, canciones=None):
    artista = {}
    artista['nombre'] = nombre.upper()
    artista['titulo'] = titulo.title()
    
    if canciones:
        artista['caciones'] = canciones
    
    return artista

flag = True

while flag:
    artista = input("Introduce tu nombre artístico: ")
        
    if artista == 'quit':
        flag = False
    else:
        titulo = input("Introduce tu título: ")        
        if titulo == 'quit':
            flag = False
        else:
            artista = hacer_album(artista, titulo)
            print(artista)
    

'''
artista_0 = hacer_album("rub3n", "Magia de Python")
artista_1 = hacer_album("ruben tercero", "Psicokiller")
artista_2 = hacer_album("r3n", "techno device", 12)

print(artista_0)
print(artista_1)
print(artista_2)
'''