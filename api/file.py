import requests

url = "https://vision.foodvisor.io/api/1.0/en/limits/"
headers = {"Authorization": "Api-Key TAHsFDAB.WJAqMmGPggyhMdgTTWlSLHANKYcncd3Q"}
response = requests.get(url, headers=headers)
response.raise_for_status()
data = response.json()

data = {'analysis': {'current': 11, 'limit': 100, 'renew_on': '2025-01-01'}}