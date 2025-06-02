import matplotlib.pyplot as plt
from die import Die

die_1 = Die()
die_2 = Die()

results = [die_1.roll() + die_2.roll() for _ in range(1000)]

max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)

frequencies = [results.count(value) for value in poss_results]
        
plt.bar(poss_results,frequencies, edgecolor='black')
plt.title("Resultados de tirar dos dados D6 - 1000 veces")
plt.xlabel("Resultado del dado")
plt.ylabel("Frecuencia del resultado")
plt.xticks(poss_results)
# px.bar(x=poss_results, y = frequencies, title="Resultados de tirar dos dados D6 y multiplicar su valor - 1000 veces", labels = {'x': 'Resultado del dado', 'y': 'Frecuencia de resultado'})
# fig.update_layout(xaxis_dtick=1)

plt.show()  
