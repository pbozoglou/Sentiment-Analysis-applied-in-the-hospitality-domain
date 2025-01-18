import numpy as np
import folium
import pandas as pd

'''
This script aims to generate a grid of coordinates for the city of Athens and surrounding areas.
For this example we start north-west and go approximately 0.5km east/south in each column/row.
We use a 20x20 grid (400 points) and also generate a map use 'folium' to visualize if the points
fit/cover the areas we want to scan for lodging in the 'get_reviews.py' script.
'''

# Starting coordinates
start_lat = 38.017383
start_lon = 23.672536

# Grid parameters
rows = 20
cols = 20
lat_delta = 0.0045
lon_delta = 0.006

# Generate grid
coords = []
for i in range(rows):
    for j in range(cols):
        lat = start_lat - (i * lat_delta)
        lon = start_lon + (j * lon_delta)
        coords.append((lat, lon))

coords_df = pd.DataFrame(coords, columns=['Latitude', 'Longitude'])
coords_df.to_csv('datasets/grid_coordinates.csv', index=False)
print("Grid generated at 'datasets/grid_coordinates.csv'.")

# Generate map for visualization
mymap = folium.Map(location=[start_lat, start_lon], zoom_start=12)
for index, row in coords_df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']]).add_to(mymap)
mymap.save('datasets/grid_map.html')
print("Map has been saved to 'datasets/grid_map.html'.")