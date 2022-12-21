
# This code will open the GeoJSON file, 
# read the contents into a Python object,
# and then iterate through the features in the file. 
# For each feature, it will extract the coordinates and print them to the screen.

# Note that this code assumes that the GeoJSON file follows the standard format 
# for a GeoJSON file, with a top-level features property that contains a list 
# of feature objects. Each feature object should have a geometry property that 
# contains the coordinates for the feature.

import json

# Open the GeoJSON file
with open('buildings.geojson', 'r') as f:
    data = json.load(f)

# Iterate through the features in the GeoJSON file
for feature in data['features']:
    # Get the coordinates of the current feature
    coordinates = feature['geometry']['coordinates']
    # Print the coordinates to the screen
    print(coordinates)
