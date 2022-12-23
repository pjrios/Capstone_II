#!/usr/bin/env python
# coding: utf-8

# This code filters the features in a GeoJSON file called Alaska.geojson based on whether their coordinates are contained within a set of polygons contained in another GeoJSON file called alaska-ra.geojson.
# 
# The code first imports the geopandas and shapely libraries. It then loads the alaska-ra.geojson file into a GeoDataFrame object called polygons_gdf using the read_file function from geopandas.
# 
# Next, it iterates over the rows of the polygons_gdf GeoDataFrame and creates a list of Polygon objects called polygons. It does this by extracting the geometry of each row using the geometry attribute, and then creating a Polygon object using the shape function from shapely.
# 
# The code then loads the Alaska.geojson file into a GeoDataFrame object called features_gdf using the read_file function.
# 
# It then iterates over the rows of the features_gdf GeoDataFrame and extracts the coordinates of each feature using the geometry attribute. It then checks if the coordinates are contained within any of the Polygon objects in the polygons list using the contains method from Shapely. If the coordinates are contained within a polygon, the feature is added to a list of filtered features called filtered_features.
# 
# Finally, the code creates a new GeoDataFrame object called filtered_gdf using the GeoDataFrame constructor and the filtered_features list. It then saves the filtered_gdf to a new GeoJSON file called filtered.geojson using the to_file function.
# 
# Finally, the code prints the number of polygons in the polygons_gdf GeoDataFrame and the number of filtered features in the filtered_features list.
# 
# This code should filter the features in the Alaska.geojson file and create a new GeoJSON file called filtered.geojson with only the features that are contained within the polygons in the alaska-ra.geojson file

# In[14]:


import geopandas as gpd
from shapely.geometry import Polygon, shape

# Load the GeoJSON file containing the polygons
polygons_gdf = gpd.read_file('alaska-ra.geojson')

# Create a list of Polygon objects
polygons = []
for row in polygons_gdf.itertuples(index=True, name='GeoPandas'):
    polygon = shape(row.geometry)
    polygons.append(polygon)

# Load the GeoJSON file with the features to filter
features_gdf = gpd.read_file('Alaska.geojson')

# Iterate over the features and extract the coordinates
filtered_features = []
for row in features_gdf.itertuples(index=True, name='GeoPandas'):
    coords = shape(row.geometry)
    #print("processing")
    # Check if the coordinates are contained within any of the polygons
    contained = False
    for polygon in polygons:
        if polygon.contains(coords):
            contained = True
            break

    # If the coordinates are contained within a polygon, add the feature to the list of filtered features
    if contained:
        filtered_features.append(row.geometry)
        
# Create a new GeoDataFrame with the filtered features
filtered_gdf = gpd.GeoDataFrame(geometry=filtered_features)

# Save the filtered features to a new GeoJSON file
filtered_gdf.to_file('filtered.geojson', driver='GeoJSON')
        
# Print the number of polygons and the number of filtered features
print(f'Number of polygons: {len(polygons_gdf)}')
print(f'Number of filtered features: {len(filtered_features)}')

