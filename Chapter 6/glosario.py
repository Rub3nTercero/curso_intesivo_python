# Autor Rubén Tercero - Fecha: 23/02/2025
# Este script imprime un glosario de palabras

glosario = {
    'variable': "Una variable en Python es un espacio en la memoria donde se almacena un valor. Su valor puede cambiar a lo largo del tiempo. Se crea simplemente asignando un valor a un nombre.",
    'función': "Una función es un bloque de código diseñado para realizar una tarea específica. Se puede definir mediante la palabra clave def, y se puede reutilizar varias veces en el programa.",
    'librería': "Una librería en Python es un conjunto de módulos que contienen funciones y métodos predefinidos, diseñados para realizar tareas específicas. ",
    'bucle': "Un bucle es una estructura de control que repite una sección de código mientras se cumpla una condición específica. ",
    'clase': "Una clase en Python es una plantilla para crear objetos. Define un conjunto de atributos y métodos que serán comunes a todas las instancias de la clase.",
}

for k, v in glosario.items():
    print(f"{k.title()}:")
    print(f"{v}\n")