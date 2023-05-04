# Residential Building Identification
To run this program, you will need the following:

1. Python 3 installed on your system.
2. The following Python libraries: geopandas, shapely, JSON, subprocess, shutil, and os.
3. The "allmapsoft" software installed on your system. If you installed it into a different directory than the default directory make sure to modify the  downloader_path and combiner_path variables in the getImages.py program.
4. The filter.py program requires directories with the GeoJSON files.
5. The getImages.py program takes GeoJSON files in the format [state_name]_filtered.geojson, where state_name is the name of the state you are processing (e.g. Alaska)
6. Read and write permissions for the specified directories States_GeoJSONs, Residential_Areas, Filtered, images, and images/results/
7. In addition, the programs assume that you have the necessary dependencies and packages installed to run the functions from the imported libraries.

## getImages.ipynb
This program is designed to read a GeoJSON file containing a set of features defined by coordinates, and use those coordinates to retrieve images from Google Maps using the downloader program form "allmapsoft". 
  ### The rest of the images can be found here: https://uark.box.com/s/o7l7nfhc8h5udn8gfmthvyx4zukzc9ma
