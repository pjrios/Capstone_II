# Residential Building Identification
## getImages.py
### <ins>Status: completed</ins>
This is the main program for this section. It is designed to read a GeoJSON file containing a set of features defined by coordinates, and use those coordinates to retrieve images from Google Maps using the downloader program form "allmapsoft". The program consists of three main parts: and does the following:

1. Read data from a Json file: It defines a function get_square_bounds that takes a polygon (a list of coordinates) as an argument and returns the coordinates of a square that bounds the polygon. The code opens a GeoJSON file and loads its contents into a variable called data. It iterates through the features in the GeoJSON file and extracts the coordinates of each feature. For each feature, the code calls the get_square_bounds function to calculate the coordinates of a bounding square for the feature.
 
2. Download and combine the images: It generates a command string that calls the "downloader.exe" program from the "allmapsoft" software, passing in the bounding square coordinates and a destination directory for the map image. The code calls the subprocess.run function to execute the command and generate the map image. It then calls the subprocess.run function again to combine the map image into a single file using the "combiner.exe" program from the "allmapsoft" software.
 
3. Clean up: It moves the combined map image from the source directory to a destination directory using the shutil.move function and then cleans up by deleting the intermediate files and directories that were created during the processing.

## filter.py
### <ins>Status: Completed </ins>
This file contains functionalities for filtering json files based on coordinates. This code filters the features in a GeoJSON file called [name].geojson based on whether their coordinates are contained within a set of polygons contained in another GeoJSON file called [name]-ra.geojson. [name] represent a variable with the name of a state.

1. The code first imports the geopandas and shapely libraries. It then loads the [name]-ra.geojson file into a GeoDataFrame object called polygons_gdf using the read_file function from geopandas. Next, it iterates over the rows of the polygons_gdf GeoDataFrame and creates a list of Polygon objects called polygons. It does this by extracting the geometry of each row using the geometry attribute, and then creating a Polygon object using the shape function from shapely. The code then loads the [name].geojson file into a GeoDataFrame object called features_gdf using the read_file function.

2. It then iterates over the rows of the features_gdf GeoDataFrame and extracts the coordinates of each feature using the geometry attribute. It then checks if the coordinates are contained within any of the Polygon objects in the polygons list using the contains method from Shapely. If the coordinates are contained within a polygon, the feature is added to a list of filtered features called filtered_features.

3. Finally, the code creates a new GeoDataFrame object called filtered_gdf using the GeoDataFrame constructor and the filtered_features list. It then saves the filtered_gdf to a new GeoJSON file called [name]_filtered.geojson using the to_file function. 
