import json
import subprocess
import shutil
import os, glob
import time
from tqdm import tqdm
from shapely.geometry import Polygon, box
from geopy.geocoders import Nominatim
from twilio.rest import Client
geolocator = Nominatim(user_agent="geoapiExercises")

# name of the state we are working with
# should we change it to an input?
state_name = 'small_alaska'
input_folder_name = "Filtered"
working_directory_path = r'C:\Users\pjrio\CapstoneII\\'
img_path = "images"
result_path = img_path + "/results" + "/"+state_name

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
    
def reverse_geocode(coordinates):
    location = geolocator.reverse(coordinates, exactly_one=True)
    address = location.raw['address']
    state = address.get('state', '')
    city = address.get('city', '')
    county = address.get('county', '')
    return f"{state}_{city}_{county}"
    
def get_square_bounds(polygon):
    # Convert the input polygon to a shapely Polygon
    shapely_polygon = Polygon(polygon[0])
    
    # Get the bounding box of the polygon
    bbox = shapely_polygon.bounds
    
    # Extract the left, right, top and bottom coordinates
    left, bottom, right, top = bbox
    return f"{left} {right} {top} {bottom}"

# Iterate through the features in the GeoJSON file

# Iterate through the features in the GeoJSON file
checkpoint_file = working_directory_path + "/checkpoint.txt"
if os.path.exists(checkpoint_file):
    with open(checkpoint_file, 'r') as f:
        start_index = int(f.readline().strip())
else:
    start_index = 0

#for num, feature in tqdm(enumerate(data['features'][start_index:]), desc="Processing data"):
for num, feature in enumerate(tqdm(data['features'][start_index:], desc='Processing data')):
#for num, feature in enumerate(data['features'][start_index:]):
    # Get the coordinates of the current feature
    coordinates = feature['geometry']['coordinates']
    i = num + start_index
    # Get the coordinates 
    # Format = [left longitude, right longitude, top latitude, bottom latitude]
    #print("i: " + str(i))
    square = get_square_bounds(coordinates)
    coord = square.strip().split(" ")
    longitude = float(coord[0].strip())
    latitude = float(coord[3].strip())
    
    coordinates = (latitude, longitude) # Example coordinates
    location_string = reverse_geocode(coordinates)
        
    filename = "{}_task{}.jpg".format(location_string, i)
    filename = filename.replace(" ", "-")
    #print(filename)
    
    # Generate command
    string = state_name + "_" + "task{}.gmid"
    result = string.format(i)
    
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
    #app = Application().start(command, backend='uia', visible=False)
    #os.system(f'start "" /B {command}')
    
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
    #app = Application().start(combine, backend='uia', visible=False)
    #os.system(f'start "" /B {combine}')
    
    # Move jpg to results folder 
    
    # Set the source and destination directories
    name   = state_name + "_" + "task{}"
    folder = name.format(i)
    img = folder + ".jpg"
    src = img_path + '/'+folder+"_combined"
    dst = result_path

    # Set the source and destination file paths
    src_file = os.path.join(src, img)
    dst_file = os.path.join(dst, filename)

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
    
    # Save the checkpoint
    with open(checkpoint_file, 'w') as f:
        f.write(str(num + start_index))

    

def send_sms(msg):
    account_sid = "AC59382650e117e848601271b65ab975a2"
    auth_token = "57bef9f61ca0a41d3283f7a22b4767f0"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+14795956938",
        from_="+18444901478",
        body=msg)

    print(message.sid)

#msg = "Finished retriving images for: {}.".format(state_name)
#send_sms(msg)
