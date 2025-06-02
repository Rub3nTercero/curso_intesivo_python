from pathlib import Path
import csv

import plotly.express as px

fires = []

# Read data as a string and convert to a Python object.
path = "C:\\Users\\rnosp\\github_rub3n\\curso_intesivo_python\\Datos\\mapping_global_datasets\\eq_data\\world_fires_7_day.csv"
with open(path, newline='', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        fires.append({
            "latitude": fila["latitude"],
            "longitude": fila["longitude"],
            "brightness": fila["brightness"],    
        })
        
latitudes, longitudes, brightnesses = [], [], []

for line in fires:
    latitudes.append(line['latitude'])
    longitudes.append(line['longitude'])
    brightnesses.append(float(line['brightness']))
    
title = "World Fires"
fig = px.scatter_geo(lat=latitudes, lon=longitudes, size=brightnesses,
                     color=brightnesses,
                     color_continuous_scale='Viridis',
                     labels={'color':'Brightness'},
                     projection='natural earth',
                     )
    
fig.show()
