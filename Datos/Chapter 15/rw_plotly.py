import plotly.express as px

from random_walk import RandomWalk

# Sigue generando caminatas nuevas mientras el progranma esté activo.
while True:
    # Crea una caminata aleatoria.
    rw = RandomWalk()
    rw.fill_walk()

    # Traza los puntos de la caminata.
    fig = px.scatter(x=rw.x_values, y=rw.y_values)
    point_numbers = range(rw.num_points)
    
    # Enfatiza el primer punto y el último.
    fig.add_scatter(x=[rw.x_values[0]], y=[rw.y_values[0]], mode='markers', marker=dict(color='green', size=10), name='Inicio')
    fig.add_scatter(x=[rw.x_values[-1]], y=[rw.y_values[-1]], mode='markers', marker=dict(color='red', size=10), name='Fin')
    
    # Elimina los ejes.
    fig.update_layout(
        xaxis_visible=False,
        yaxis_visible=False,
        showlegend=True,
        title='Caminata Aleatoria'
    )
    
    fig.show()
    