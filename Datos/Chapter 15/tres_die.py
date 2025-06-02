from die import Die
import plotly.express as px

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []

for roll_num in range(1_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)  
    
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
    poss_results = range(3, max_result + 1)
    for values in poss_results:
        frequency = results.count(values)
        frequencies.append(frequency)
        
fig = px.bar(x=poss_results, y = frequencies, title="Resultados de tirar tres dados D6 - 1000 veces", labels = {'x': 'Resultado del dado', 'y': 'Frecuencia de resultado'})
fig.update_layout(xaxis_dtick=1)

fig.show()  

