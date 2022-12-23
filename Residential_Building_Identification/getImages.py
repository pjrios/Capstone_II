#!/usr/bin/env python
# coding: utf-8

# This program is designed to read a GeoJSON file containing a set of features defined by coordinates, and use those coordinates to retrieve images from Google Maps using the downloader.exe program. The program consists of three main parts:
# 
# The get_square_bounds function: This function takes a polygon defined by a list of coordinates in the format [[[longitude1, latitude1], [longitude2, latitude2], ...]] and returns a string with the coordinates of a square enclosing the polygon, with each coordinate separated by a space. The function first extracts the coordinates from the polygon and calculates the bounding box of the polygon. It then calculates the center point of the bounding box and the side length of the square, and finally returns the coordinates of the square as a string.
# 
# The main block of code: This block of code opens the specified GeoJSON file, reads the contents of the file into a Python object, and iterates over the features in the file. For each feature, it gets the coordinates of the feature and passes them to the get_square_bounds function to calculate the coordinates of the square enclosing the feature. It then generates a command to run the downloader.exe program using the coordinates of the square and a specified output directory, and calls subprocess.run to execute the command. It then calls the combiner.exe program to combine the images downloaded by downloader.exe into a single file, and finally cleans up the output directory by deleting the subdirectories created by downloader.exe.
# 
# The clean.bat script: This script is called at the end of the main block of code and is used to delete the files in the output that were created by downloader.exe but that we are not going to use.

# In[11]:


import json
import subprocess
import shutil
import os

def get_square_bounds(polygon):
    # Extract the coordinates from the polygon
    coordinates = polygon[0]

    # Calculate the bounding box of the polygon
    min_lat = min(coord[1] for coord in coordinates)
    min_lng = min(coord[0] for coord in coordinates)
    max_lat = max(coord[1] for coord in coordinates)
    max_lng = max(coord[0] for coord in coordinates)

    # Calculate the center point of the bounding box
    center_lat = (min_lat + max_lat) / 2
    center_lng = (min_lng + max_lng) / 2

    # Calculate the side length of the square
    side_length = max(max_lat - min_lat, max_lng - min_lng)

    # Calculate the coordinates of the square
    left = center_lng - side_length / 2
    right = center_lng + side_length / 2
    top = center_lat + side_length / 2
    bottom = center_lat - side_length / 2

    # Return the square as a tuple of coordinates
    return f"{left} {right} {top} {bottom}"

# Open the GeoJSON file
#small_Alaska.geojson only contains some coordinates 
with open('small_Alaska.geojson', 'r') as f:
    data = json.load(f)
    
# Iterate through the features in the GeoJSON file
i = 0
for feature in data['features']:
    # Get the coordinates of the current feature
    coordinates = feature['geometry']['coordinates']
    
    # Print the coordinates to the screen as (left longitude, right longitude, top latitude, bottom latitude)
    square = get_square_bounds(coordinates)
    
    # Generate command
    string = "task{}.gmid"
    result = string.format(i)
    
    command =r'"C:\allmapsoft\gsmd\downloader.exe" "'+ result +"\" 1 21 "+square +" "+ r'"C:\Users\pjrio\CapstoneII\images"'
    #print(command)

    # Call cmd and run program
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # combine results "C:\allmapsoft\gsmd\combiner.exe" "C:\downloads\test.gmid" jpg,tif,mbtiles,gpkg meters
    combine = r'"C:\allmapsoft\gsmd\combiner.exe" ' + r'"C:\Users\pjrio\CapstoneII\images'+"\\"+ result +"\" jpg meters"
    #print(combine)
    subprocess.run(combine, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Clean
    # -----Generate command to delete path
    name = "task{}"
    folder = name.format(i)
    folder_path = r'C:/Users/pjrio/CapstoneII/images'+"/"+ folder 
    #print(folder_path)
    
    # -----Use the remove function to delete the path
    shutil.rmtree(folder_path)
            
    #increase counter
    i = i + 1

# path to the batch script
script_path = 'C:/Users/pjrio/CapstoneII/images/clean.bat'

# Run the batch script using the call function
subprocess.call([script_path])
    
    

