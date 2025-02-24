# Autor: Rubén Tercero - 25/02/2025

responses = {}

flag = True

while flag:
    usuario = input("¿Cómo te llamas? ")
    lugar = input("Si puedieras visitar cualquier lugar del mundo, ¿dónde irías? ")
    
    responses[usuario] = lugar
    
    continuar = input("¿Deseas continuar con la encuesta? ")
    
    if continuar.lower() == 'no':
        flag = False
    
for k, v in responses.items():
    print(f"{k.title()} se iría a {v.title()}")
    