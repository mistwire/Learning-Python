# A query string is a way to pass data to a server as part of a GET request
# example: http://www.example.com/?key1=value1&key2=value2

'''
Info for this bit found here:
https://icanhazdadjoke.com/api
'''


import requests 


url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term":"cat"}
    )

data = response.json() #take the JSON response (which is a string) and turn it into a dict that python can use

# print(data["joke"])
# print(f"status: {data['status']}")

print(data, '\n')
print(data['results'])