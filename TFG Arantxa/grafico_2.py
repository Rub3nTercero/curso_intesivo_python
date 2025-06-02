import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Carga y estructuración de datos
# ----------------------------
data = {
    "Ítem": list(range(1, 21)),
    "Nunca": [5, 0, 6, 4, 2, 0, 3, 0, 5, 3, 1, 0, 2, 1, 4, 5, 1, 0, 4, 0],
    "Pocas veces": [0, 1, 2, 3, 2, 1, 4, 2, 2, 6, 2, 0, 4, 2, 4, 2, 2, 1, 1, 0],
    "Algunas veces": [2, 5, 1, 2, 2, 1, 0, 3, 2, 0, 4, 2, 2, 3, 1, 1, 2, 1, 2, 1],
    "Muchas veces": [0, 2, 1, 0, 2, 3, 2, 5, 1, 0, 2, 3, 1, 2, 1, 1, 3, 3, 1, 3],
    "Siempre": [3, 2, 0, 1, 2, 5, 1, 0, 0, 1, 1, 5, 1, 2, 0, 1, 2, 5, 2, 6],
    "Media": [2.6, 3.5, 1.7, 2.1, 3, 4.2, 2.4, 3.3, 1.9, 2, 3, 4.3, 2.5, 3.2, 1.9, 2.1, 3.3, 4.2, 2.6, 4.5],
    "Dimensiones": [
        "Motivación intrínseca", "Motivación extrínseca", "Atención y concentración", "Gestión emocional",
        "Clima emocional del aula", "Preferencia por estrategias neuroeducativas", "Motivación intrínseca",
        "Motivación extrínseca", "Atención y concentración", "Gestión emocional", "Clima emocional del aula",
        "Preferencia por estrategias neuroeducativas", "Motivación intrínseca", "Motivación extrínseca",
        "Atención y concentración", "Gestión emocional", "Clima emocional del aula",
        "Preferencia por estrategias neuroeducativas", "Motivación intrínseca", "Preferencia por estrategias neuroeducativas"
    ]
}

df = pd.DataFrame(data)

# ----------------------------
# Cálculo de medias por dimensión
# ----------------------------
dimension_means = df.groupby("Dimensiones")["Media"].mean().sort_values()

# ----------------------------
# Visualización profesional
# ----------------------------
plt.figure(figsize=(10, 6))
bars = plt.barh(dimension_means.index, dimension_means.values, color = "#89CFF0")

# Títulos y etiquetas con estilo profesional
plt.title("Media por Dimensión Evaluada", fontsize=14, fontweight='bold')
plt.xlabel("Media", fontsize=12)
# plt.ylabel("Dimensión", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='x', linestyle='--', alpha=0.6)

# Mostrar valores numéricos en cada barra
for bar in bars:
    width = bar.get_width()
    '''
    plt.text(width + 0.1, bar.get_y() + bar.get_height() / 2,
             f'{width:.2f}', va='center', fontsize=10)
    '''

plt.tight_layout()

# ----------------------------
# Guardado opcional del gráfico
# ----------------------------
# Descomenta esta línea si quieres guardar el gráfico como imagen para el anexo
plt.savefig("media_dimensiones_tfg.png", dpi=300, bbox_inches='tight')

plt.show()
