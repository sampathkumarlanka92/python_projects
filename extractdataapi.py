import requests
import json

response = requests.get("https://gmail.googleapis.com/$discovery/rest?version=v1")

d = response.text
data = json.loads(d)

description = data["description"]
print(f"Description: {description}")

key_description = data["parameters"]["key"]["description"]
print(f"Key Description: {key_description}")
