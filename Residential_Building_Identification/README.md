# Residential Building Identification

## File: getImages
This is the main program for this section. It is designed to read a GeoJSON file containing a set of features defined by coordinates, and use those coordinates to retrieve images from Google Maps using the downloader.exe program. The program consists of three main parts: and does the following:

1. The get_square_bounds function: This function takes a polygon defined by a list of coordinates in the format [[[longitude1, latitude1], [longitude2, latitude2], ...]] and returns a string with the coordinates of a square enclosing the polygon, with each coordinate separated by a space. The function first extracts the coordinates from the polygon and calculates the bounding box of the polygon. It then calculates the center point of the bounding box and the side length of the square, and finally returns the coordinates of the square as a string.

2. The main block of code: This block of code opens the specified GeoJSON file, reads the contents of the file into a Python object, and iterates over the features in the file. For each feature, it gets the coordinates of the feature and passes them to the get_square_bounds function to calculate the coordinates of the square enclosing the feature. It then generates a command to run the downloader.exe program using the coordinates of the square and a specified output directory, and calls subprocess.run to execute the command. It then calls the combiner.exe program to combine the images downloaded by downloader.exe into a single file, and finally cleans up the output directory by deleting the subdirectories created by downloader.exe.

3. The clean.bat script: This script is called at the end of the main block of code and is used to delete the files in the output that were created by downloader.exe but that we are not going to use. 

## Other files
The rest of the files include the individual  functionalities such as: reading and filtering json files. 
