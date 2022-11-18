#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/waitlist"

resp= requests.get(URL)

print("Current waitlist:")
# pretty-print the response back from our POST request
pprint(resp.json())

