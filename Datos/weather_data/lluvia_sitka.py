from pathlib import Path
from datetime import datetime
from collections import defaultdict

import csv
import plotly.express as px
import pandas as pd


def datos(path, index):
    path = Path(path)

    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header = next(reader)
    # print(header)

    monthly_precip = defaultdict(float)

    for row in reader:
        try:
            date = datetime.strptime(row[2], '%Y-%m-%d')
            value = float(row[index])
            month_key = date.strftime('%Y-%m')
            monthly_precip[month_key] += value
        except ValueError:
            continue  
        
        
    months = sorted(monthly_precip)
    precipitation = [monthly_precip[month] for month in months]
    return precipitation, months

precipitation_desierto, _ = datos('C:\\Users\\rnosp\\github_rub3n\\curso_intesivo_python\\Datos\\weather_data\\death_valley_2021_full.csv', 3)
precipitation_sitka, months = datos('C:\\Users\\rnosp\\github_rub3n\\curso_intesivo_python\\Datos\\weather_data\\sitka_weather_2021_full.csv', 5)

df = pd.DataFrame({
    'Mes': months * 2,
    'Ciudad': ['Sitka'] * len(months) + ['Death Valley'] * len(months),
    'Precipitación': precipitation_sitka + precipitation_desierto
})

# Visualizar los resultados
title = "Cantitad de lluvias diarias en 2021"
label = { 'x': 'Mes', 'y': 'Cantidad de lluvia'}
fig = px.bar(df, x='Mes', y='Precipitación', color='Ciudad', barmode='group', title=title, labels=label)
fig.update_layout(
    xaxis = dict(
        tickformat= "%b %Y",
        tickangle=45,
        tickmode='linear',
        dtick="M1"
    )
)
fig.show()
    

    


