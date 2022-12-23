#!/usr/bin/env python
# coding: utf-8

# This is the main program for this section. It is designed to read a GeoJSON file containing a set of features defined by coordinates, and use those coordinates to retrieve images from Google Maps using the downloader program form "allmapsoft". The program consists of three main parts: and does the following:
# 
# 1. Read data from a Json file: It defines a function get_square_bounds that takes a polygon (a list of coordinates) as an argument and returns the coordinates of a square that bounds the polygon. The code opens a GeoJSON file and loads its contents into a variable called data. It iterates through the features in the GeoJSON file and extracts the coordinates of each feature. For each feature, the code calls the get_square_bounds function to calculate the coordinates of a bounding square for the feature.
# 
# 2. Download and combine the images: It generates a command string that calls the "downloader.exe" program from the "allmapsoft" software, passing in the bounding square coordinates and a destination directory for the map image. The code calls the subprocess.run function to execute the command and generate the map image. It then calls the subprocess.run function again to combine the map image into a single file using the "combiner.exe" program from the "allmapsoft" software.
# 
# 3. Clean up: It moves the combined map image from the source directory to a destination directory using the shutil.move function and then it cleans up by deleting the intermediate files and directories that were created during the processing.

# In[41]:


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
    
    # Move jpg to results folder 
    
    # Set the source and destination directories
    name = "task{}"
    folder = name.format(i)
    img = folder + ".jpg"
    src = 'C:/Users/pjrio/CapstoneII/images/'+folder+"_combined"
    dst = 'C:/Users/pjrio/CapstoneII/images/results'

    # Set the source and destination file paths
    src_file = os.path.join(src, img)
    dst_file = os.path.join(dst, img)

    # Use the shutil module to move the file
    shutil.move(src_file, dst_file)
    
    # Clean
    # -----Generate command to delete path
    folder_path = r'C:/Users/pjrio/CapstoneII/images'+"/"+ folder 
    combined_folder_path = r'C:/Users/pjrio/CapstoneII/images'+"/"+ folder+"_combined"
    #print(folder_path)
    
    # -----Use the remove function to delete the path
    shutil.rmtree(folder_path)
    shutil.rmtree(combined_folder_path)      
    #increase counter
    i = i + 1

# path to the batch script
script_path = 'C:/Users/pjrio/CapstoneII/images/clean.bat'

# Run the batch script using the call function
subprocess.call([script_path])
    
