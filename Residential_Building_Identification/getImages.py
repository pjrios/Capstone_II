#!/usr/bin/env python
# coding: utf-8

# This code processes a GeoJSON file and generates map images using the "allmapsoft" software.
# 
# Here is an overview of what the code does:
# 
# 1. The code imports several modules that it will use later: json, subprocess, shutil, os and shapely.
# 
# 2. It defines a function get_square_bounds that takes a polygon (a list of coordinates) as an argument and returns the coordinates of a square that bounds the polygon.
# 
# 3. The code opens the GeoJSON file [state_name].geojson and loads its contents into a variable called data.
# 
# 4. It iterates through the features in the GeoJSON file and extracts the coordinates of each feature.
# 
# 5. For each feature, the code calls the get_square_bounds function to calculate the coordinates of a bounding square for the feature.
# 
# 6. It generates a command string that calls the "downloader.exe" program from the "allmapsoft" software, passing in the bounding square coordinates and a destination directory for the map image.
# 
# 7. The code calls the subprocess.run function to execute the command and generate the map image.
# 
# 8. It then calls the subprocess.run function again to combine the map image into a single file using the "combiner.exe" program from the "allmapsoft" software.
# 
# 9. It moves the combined map image from the source directory to a destination directory using the shutil.move function.
# 
# 10. It cleans up by deleting the intermediate files and directories that were created during the processing.

# In[3]:

import json
import subprocess
import shutil
import os, glob
import time
from shapely.geometry import Polygon, box


# name of the state we are working with
# should we change it to an input?
state_name = 'small_alaska'
input_folder_name = "Filtered"
working_directory_path = r'C:\Users\pjrio\CapstoneII\\'
img_path = "images"
result_path = img_path + "/results"

# name of the filtered file based on state name example: alaska_filtered.geojson
# [state_name]_filtered.geojson is the file generate it for each state during the filtering process
filtered_file_path = input_folder_name + "/" + state_name + "_filtered.geojson"

# Note: This paths might need to be change depending on where you installed the software
# paths for allmapsoft program
downloader_path  = r'"C:\allmapsoft\gsmd\downloader.exe" '
combiner_path    = r'"C:\allmapsoft\gsmd\combiner.exe" '

# Note: You need to change this path !!!
# This is the output path for the google maps image dowloader and it needs a full path to work
destination_path = working_directory_path + img_path

if not os.path.exists(img_path):
    os.makedirs(img_path)
    
if not os.path.exists(result_path):
    os.makedirs(result_path)
    
# Open the GeoJSON file
#small_Alaska.geojson only contains some coordinates 
with open(filtered_file_path, 'r') as f:
    data = json.load(f)
    
def get_square_bounds(polygon):
    # Convert the input polygon to a shapely Polygon
    shapely_polygon = Polygon(polygon[0])
    
    # Get the bounding box of the polygon
    bbox = shapely_polygon.bounds
    
    # Extract the left, right, top and bottom coordinates
    left, bottom, right, top = bbox
    return f"{left} {right} {top} {bottom}"

# Iterate through the features in the GeoJSON file
i = 0
for feature in data['features']:
    # Get the coordinates of the current feature
    coordinates = feature['geometry']['coordinates']
    
    # Get the coordinates 
    # Format = [left longitude, right longitude, top latitude, bottom latitude]
    square = get_square_bounds(coordinates)
    
    # Generate command
    string = state_name + "_" + "task{}.gmid"
    result = string.format(i)
    img_name = state_name + "_" + "task{}.jpg"
    img_name = img_name.format(i)
    
    #"C:\allmapsoft\gsmd\downloader.exe" para1 para2 para3 para4 para5 para6 para7 para8
    # para1: task name(only filename, without path)
    # para2: maps type
    # para3: zoom level
    # para4: left longitude
    # para5: right longitude
    # para6: top latitude
    # para7: bottom latitude
    # para8: path to save
    # Example: "C:\allmapsoft\gsmd\downloader.exe" "test.gmid" 1 12 2 3 49 48 "C:\downloads"
    para2 = "1"
    para3 = "21"
    #NOTE: I am not sure if i selected the ideal configuration so we might want to look into that
    command = downloader_path + '"'+result +'\" ' + para2 +" "+ para3 + " "+ square +' "'+ destination_path +'"'
    #print(command)

    # Call cmd and run downloader program
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # "C:\allmapsoft\gsmd\combiner.exe" para1 para2 para3
    # para1:task name(full path)
    # para2:output types(separated with comma)
    # para3:extent unit ("meters" or "degrees")

    # combine results "C:\allmapsoft\gsmd\combiner.exe" "C:\downloads\test.gmid" jpg,tif,mbtiles,gpkg meters
    
    #NOTE: Same thing here. I am not sure if i selected the ideal configuration so we might want to look into that
    combine = combiner_path +'"' + destination_path +"\\"+ result +"\" jpg meters"
    #print(combine)
    
    # Call cmd and run combine program
    subprocess.run(combine, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Move jpg to results folder 
    
    # Set the source and destination directories
    name   = state_name + "_" + "task{}"
    folder = name.format(i)
    img = folder + ".jpg"
    src = img_path + '/'+folder+"_combined"
    dst = result_path

    # Set the source and destination file paths
    src_file = os.path.join(src, img)
    dst_file = os.path.join(dst, img)

    # Use the shutil module to move the file
    shutil.move(src_file, dst_file)
    
    # uncomment to see the running time
    #start = time.time()
    
    # Clean
    # -----Generate command to delete path
    folder_path = img_path + "/" + folder 
    combined_folder_path = img_path +"/"+ folder+"_combined"
    
    # -----Use the remove function to delete the path
    shutil.rmtree(folder_path)
    shutil.rmtree(combined_folder_path)

    #increase counter
    i = i + 1

    # Use glob to get a list of all the files in the directory
    del_dir = working_directory_path +"/"+ img_path
    files   = glob.glob(del_dir + '/*')

    # Iterate over the list of files and delete them one by one
    for file in files:
        if os.path.isfile(file):
            # If it's a regular file, delete it
            os.remove(file)
        
    #end = time.time()
    #print(f'Running time: {end - start} seconds')

