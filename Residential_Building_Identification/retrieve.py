# This code will send a request to the Google 
# Maps Static API using the requests library, 
# and retrieve the map image in response. It 
# will then save the image to a file on your 
# local machine.

# To use this code, you will need to obtain an 
# API key from the Google Cloud Console and 
# replace the YOUR_API_KEY placeholder with 
# your own key. You can also customize the 
# location, zoom level, size, and map type 
# by modifying the corresponding variables 
# in the code.

import requests

# Set the coordinates for the location
lat = 40.7128
lng = -74.0060

# Set the zoom level for the map (0-22)
zoom = 12

# Set the size of the map image
size = "640x640"

# Set the type of map (roadmap, satellite, hybrid, terrain)
maptype = "roadmap"

# Set the API key (obtain one from the Google Cloud Console)
api_key = "YOUR_API_KEY"

# Construct the URL for the static map image
url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom={zoom}&size={size}&maptype={maptype}&key={api_key}"

# Send a request to the URL and retrieve the image
response = requests.get(url)
image = response.content

# Save the image to a file
with open("map.png", "wb") as f:
    f.write(image)