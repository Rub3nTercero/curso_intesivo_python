from die import Die
import plotly.express as px

die_1 = Die()
die_2 = Die()

results = [die_1.roll() * die_2.roll() for _ in range(1000)]

max_result = die_1.num_sides * die_2.num_sides
poss_results = range(1, max_result + 1)

frequencies = [results.count(value) for value in poss_results]
        
fig = px.bar(x=poss_results, y = frequencies, title="Resultados de tirar dos dados D6 y multiplicar su valor - 1000 veces", labels = {'x': 'Resultado del dado', 'y': 'Frecuencia de resultado'})
fig.update_layout(xaxis_dtick=1)

fig.show()  

