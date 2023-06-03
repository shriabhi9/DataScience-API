# TMDb 2.1
# Send Feedback
# Find the name and birthplace of the present most popular person according to TMDb API.
# Output Format:
# id
# name - birthplace

import requests
api_key = "YOUR_API"
api_link = "https://api.themoviedb.org/3"
header = {'Accept': 'application/json'}
params = {'api_key':api_key , "language" : "en-US"}
response = requests.get(api_link + "/person/popular", headers = header, params = params)
data = response.json()
results = data['results'][0]['id']
print(results)



response = requests.get("https://api.themoviedb.org/3/person/"+str(results),params = params) 
data = response.json()
print(data["name"],end=" - ")
print(data["place_of_birth"])



