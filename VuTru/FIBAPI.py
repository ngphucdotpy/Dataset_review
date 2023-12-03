import requests
import json

response = requests.get('https://api.fbi.gov/wanted/v1/list')
data = json.loads(response.content)
print(data['total'])
# Print list of keys
print(data['items'][0].keys())
