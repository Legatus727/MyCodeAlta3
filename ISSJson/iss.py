#!/usr/bin/env python3

import requests

URL = "http://api.open-notify.org/iss-now.json"

resp = requests.get(URL).json()

# SOLUTION TO PART 2
lon= resp["iss_position"]["longitude"]
lat= resp["iss_position"]["latitude"]

print(f"""
CURRENT LOCATION OF THE ISS:
Lon: {lon}
Lat: {lat}
""")
