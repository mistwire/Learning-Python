import requests

url = "https://icanhazdadjoke.com"
response = requests.get(url, headers={"Accept": "application/json"})

data = response.json() #take the JSON response (which is a string) and turn it into a dict that python can use

print(response.text)
print(response.json())

print(type(response))
print(type(data)) # this is a dict 

print(data)
print(data["joke"])

print(f"status: {data['status']}")

year = 2016
month = "December"
name = "PyBites"

# Type your print statement below this line

print(f"{name} was founded in {month} {year}")