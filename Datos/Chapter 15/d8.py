from die import Die
import plotly.express as px

die_1 = Die(8)
die_2 = Die(8)

results = []

for roll_num in range(20_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)  
    
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    poss_results = range(2, max_result + 1)
    for values in poss_results:
        frequency = results.count(values)
        frequencies.append(frequency)
        
fig = px.bar(x=poss_results, y = frequencies, title="Resultados de tirar dos dados D8 - 20000 veces", labels = {'x': 'Resultado del dado', 'y': 'Frecuencia de resultado'})
fig.update_layout(xaxis_dtick=1)

fig.show()  

