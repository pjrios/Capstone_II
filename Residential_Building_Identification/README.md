# Residential Building Identification
To run this programs, you will need the following:

1. Python 3 installed on your system.
2. The following Python libraries: geopandas, shapely, json, subprocess, shutil, and os.
3. The "allmapsoft" software installed on your system. If you installed it into a diferent directory than the default directory make sure to modify the  downloader_path and combiner_path variable in the getImages.py program.
4. The filter.py program requires directories with the GeoJSON files.
5. The getImages.py program takes GeoJSON files in the format [state_name]_filtered.geojson, where state_name is the name of the state you are processing (e.g. alaska)
6. Read and write permissions for the specified directories States_GeoJSONs, Residential_Areas, Filtered, images, and images/results/
7. In addition, the programs assume that you have the necessary dependencies and packages installed to run the functions from the imported libraries.
## getImages.py
This program is designed to read a GeoJSON file containing a set of features defined by coordinates, and use those coordinates to retrieve images from Google Maps using the downloader program form "allmapsoft". 
### The rest of the images can be found here: https://uark.box.com/s/h6898oyvnkbumb3ix2y2fufk2nykhr5u

## filter.py
This file contains functionalities for filtering json files based on coordinates. This code filters the features in a GeoJSON file called [name].geojson based on whether their coordinates are contained within a set of polygons contained in another GeoJSON file called [name]-ra.geojson. [name] represent a variable with the name of a state.

