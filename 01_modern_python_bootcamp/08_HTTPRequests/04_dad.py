# API project - asks for a joke topic & returns searched jokes from icanhazdadjokes.com

import requests
user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url, 
    headers ={"Accept": "application/json"},
    params={"term":user_input}
).json()

num_jokes = res["total_jokes"]


