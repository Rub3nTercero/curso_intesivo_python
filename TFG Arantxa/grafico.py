# Volver a crear el gráfico profesional ahora que df está definido

import matplotlib.pyplot as plt
import pandas as pd

# Crear gráfico de barras apiladas por ítem

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
fig, ax = plt.subplots(figsize=(14, 8))
categories = ["Nunca", "Pocas veces", "Algunas veces", "Muchas veces", "Siempre"]
bar_data = df.set_index("Ítem")[categories]

# Colores profesionales por categoría
colors = ['#ff1493', '#CDA4DE', '#fff4b1', '#89cff0', '#40e0d0']  # Tonos cálidos a fríos

# Crear gráfico apilado con colores personalizados
bar_data.plot(kind="bar", stacked=True, ax=ax, color=colors, edgecolor='black')

# Añadir etiquetas a cada segmento de la barra si el valor es distinto de 0
for i, item in enumerate(bar_data.index):
    y_offset = 0
    for j, category in enumerate(categories):
        value = bar_data.loc[item, category]
        if value != 0:
            ax.text(i, y_offset + value / 2, str(value), ha='center', va='center', fontsize=9, color='black')
        y_offset += value

# Personalización del gráfico
ax.set_title("Distribución de respuestas por ítem del cuestionario", fontsize=16, fontweight='bold')
ax.set_xlabel("Ítem", fontsize=12)
# ax.set_ylabel("Número de respuestas", fontsize=12)
ax.tick_params(axis='x', rotation=0)
ax.tick_params(axis='both', labelsize=10)
ax.legend(title="Frecuencia de respuesta", title_fontsize=11, fontsize=10, bbox_to_anchor=(1.02, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.savefig("distribucion_item.png", dpi=300, bbox_inches='tight')

# Mostrar gráfico
plt.show()
