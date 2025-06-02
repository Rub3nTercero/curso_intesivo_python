from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt
from datetime import datetime

# path = Path('C:\\Users\\rnosp\\github_rub3n\\curso_intesivo_python\\Datos\\weather_data\\sitka_weather_2021_full.csv')
path = Path('C:\\Users\\rnosp\\github_rub3n\\curso_intesivo_python\\Datos\\weather_data\\death_valley_2021_full.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

date_index = header_row.index('DATE')
high_index = header_row.index('TMAX')
low_index = header_row.index('TMIN')
name_index = header_row.index('NAME')

dates, highs, lows = [], [], []

for row in reader:
    current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    try:
        high = int(row[high_index])
        low = int(row[low_index])
    except ValueError:
        print(f"Dato perdido en {current_date}")
        continue
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = f"Temperaturas altas y bajas - 2021\n{row[name_index]}"
ax.set_title(title, fontsize=20)
ax.set_xlabel('')

ax.set_ylim(0, 200)

plt.show()
    
    