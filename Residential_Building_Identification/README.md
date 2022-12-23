# Residential Building Identification

## File: Arkansas_residential-areas_GeoJSON.zip
This zip contains a GeoJson file of the resindetial areas in arkansas retrieved using the following website: https://export.hotosm.org/en/v3/exports/new/describe

## Microsoft Building Footprints Datasets
The Microsoft Building Footprints datsets can be found here: https://github.com/Microsoft/USBuildingFootprints

## File: getImages.py
This is the main program for this section. It is designed to read a GeoJSON file containing a set of features defined by coordinates, and use those coordinates to retrieve images from Google Maps using the downloader program form "allmapsoft". The program consists of three main parts: and does the following:

1.Read data from a Json file: It defines a function get_square_bounds that takes a polygon (a list of coordinates) as an argument and returns the coordinates of a square that bounds the polygon. The code opens a GeoJSON file and loads its contents into a variable called data. It iterates through the features in the GeoJSON file and extracts the coordinates of each feature. For each feature, the code calls the get_square_bounds function to calculate the coordinates of a bounding square for the feature.
 
2.Download and combine the images: It generates a command string that calls the "downloader.exe" program from the "allmapsoft" software, passing in the bounding square coordinates and a destination directory for the map image. The code calls the subprocess.run function to execute the command and generate the map image. It then calls the subprocess.run function again to combine the map image into a single file using the "combiner.exe" program from the "allmapsoft" software.
 
3.Clean up: It moves the combined map image from the source directory to a destination directory using the shutil.move function and then cleans up by deleting the intermediate files and directories that were created during the processing.

## Other files
The rest of the files include the individual  functionalities such as: reading and filtering json files. 
