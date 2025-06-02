import matplotlib.pyplot as plt

# input_values = range(1, 6)
input_values = range(1, 5001)
output_values = [x**3 for x in input_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(input_values, output_values,c=output_values, cmap=plt.cm.Blues, s=10)
#ax.plot(input_values, output_values, c=output_values)

ax.set_title('Números Cúbicos', fontsize=24)
ax.set_xlabel('Valor base', fontsize=14)
ax.set_ylabel('Valor cúbico', fontsize=14)

ax.axis([0, 5100, 0, 130_000_000_000])

ax.tick_params(labelsize=14)
#ax.ticklabel_format(style='plain')

plt.show()
# plt.savefig('numeros_cubicos.png', bbox_inches='tight')


