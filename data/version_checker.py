import requests
import json


url = 'https://github.com/caligola25/DEILabs/data/version.json'
f = requests.get(url)
# The .json() method automatically parses the response into JSON.
git_version = f.json()

with open('data/version.json') as f:
    version = json.load(f)

if git_version["version"] > version["version"]:
    print("Update available")
else:
    print("")