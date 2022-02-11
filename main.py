import requests
from pprint import pprint

r = requests.get("https://jsonplaceholder.typicode.com/users")
data = r.json()

pprint(data)